#!/usr/bin/env python3
"""Send one 2D NavigateToPose goal and report feedback/result state.

Validation scope:
- Python syntax/static structure: checked before publication.
- ROS 2 Humble package build: not included in the published evidence.
- Nav2 simulator / real TurtleBot3 integration: not included in the published evidence.

The qz/qw conversion below assumes planar motion with roll=pitch=0 and yaw in radians.
"""

from __future__ import annotations

import math
from typing import Any

import rclpy
from action_msgs.msg import GoalStatus
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from rclpy.node import Node


class NavigateToPoseClient(Node):
    """Send one map-frame goal, optionally request cancel, then exit cleanly."""

    def __init__(self) -> None:
        super().__init__("navigate_to_pose_client")

        self.declare_parameter("x", 1.0)
        self.declare_parameter("y", 0.0)
        self.declare_parameter("yaw", 0.0)
        self.declare_parameter("frame_id", "map")
        self.declare_parameter("action_name", "navigate_to_pose")
        self.declare_parameter("behavior_tree", "")
        self.declare_parameter("server_timeout_sec", 5.0)
        self.declare_parameter("cancel_after_sec", 0.0)

        self._done = False
        self._goal_handle: Any | None = None
        self._cancel_timer: Any | None = None
        self._cancel_after_sec = 0.0

        action_name = str(self.get_parameter("action_name").value).strip()
        if not action_name:
            raise ValueError("action_name parameter must not be empty")

        self._client = ActionClient(self, NavigateToPose, action_name)

    @property
    def done(self) -> bool:
        """Return True after terminal failure or final Action result."""
        return self._done

    def send_configured_goal(self) -> bool:
        """Read parameters, validate them, and start the asynchronous goal flow."""
        x = float(self.get_parameter("x").value)
        y = float(self.get_parameter("y").value)
        yaw = float(self.get_parameter("yaw").value)
        frame_id = str(self.get_parameter("frame_id").value).strip()
        behavior_tree = str(self.get_parameter("behavior_tree").value).strip()
        server_timeout_sec = float(self.get_parameter("server_timeout_sec").value)
        cancel_after_sec = float(self.get_parameter("cancel_after_sec").value)

        numeric_values = {
            "x": x,
            "y": y,
            "yaw": yaw,
            "server_timeout_sec": server_timeout_sec,
            "cancel_after_sec": cancel_after_sec,
        }
        invalid = [name for name, value in numeric_values.items() if not math.isfinite(value)]
        if invalid:
            self.get_logger().error(f"Non-finite parameter(s): {', '.join(invalid)}")
            self._finish()
            return False
        if not frame_id:
            self.get_logger().error("frame_id parameter must not be empty")
            self._finish()
            return False
        if server_timeout_sec <= 0.0:
            self.get_logger().error("server_timeout_sec must be greater than 0")
            self._finish()
            return False
        if cancel_after_sec < 0.0:
            self.get_logger().error("cancel_after_sec must be 0 or greater")
            self._finish()
            return False

        if not self._client.wait_for_server(timeout_sec=server_timeout_sec):
            self.get_logger().error(
                "NavigateToPose Action server was not found within "
                f"{server_timeout_sec:.1f} s. Check launch, lifecycle, Domain, "
                "namespace, and action_name."
            )
            self._finish()
            return False

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = frame_id
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y
        goal.pose.pose.position.z = 0.0
        goal.pose.pose.orientation.x = 0.0
        goal.pose.pose.orientation.y = 0.0
        goal.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal.pose.pose.orientation.w = math.cos(yaw / 2.0)
        if behavior_tree:
            goal.behavior_tree = behavior_tree

        self.get_logger().info(
            f"Goal send request: frame={frame_id}, x={x:.3f}, y={y:.3f}, yaw={yaw:.3f} rad"
        )
        self._cancel_after_sec = cancel_after_sec
        send_future = self._client.send_goal_async(
            goal,
            feedback_callback=self._feedback_callback,
        )
        send_future.add_done_callback(self._goal_response_callback)
        return True

    def _feedback_callback(self, feedback_msg: Any) -> None:
        feedback = feedback_msg.feedback
        distance = getattr(feedback, "distance_remaining", float("nan"))
        recoveries = getattr(feedback, "number_of_recoveries", -1)
        self.get_logger().info(
            f"Feedback: distance_remaining={distance:.2f} m, recoveries={recoveries}"
        )

    def _goal_response_callback(self, future: Any) -> None:
        try:
            goal_handle = future.result()
        except Exception as exc:  # middleware/future errors are runtime-dependent
            self.get_logger().error(f"Goal response failed: {exc}")
            self._finish()
            return

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("Goal Rejected: server did not accept the goal.")
            self._finish()
            return

        self._goal_handle = goal_handle
        self.get_logger().info("Goal Accepted: execution has started (not yet success).")

        if self._cancel_after_sec > 0.0:
            self._cancel_timer = self.create_timer(
                self._cancel_after_sec,
                self._request_cancel_once,
            )

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_callback)

    def _request_cancel_once(self) -> None:
        if self._cancel_timer is not None:
            self.destroy_timer(self._cancel_timer)
            self._cancel_timer = None

        if self._goal_handle is None:
            self.get_logger().warning("No accepted goal is available for cancellation.")
            return

        self.get_logger().warning("Sending cancel request.")
        cancel_future = self._goal_handle.cancel_goal_async()
        cancel_future.add_done_callback(self._cancel_response_callback)

    def _cancel_response_callback(self, future: Any) -> None:
        try:
            response = future.result()
        except Exception as exc:
            self.get_logger().error(f"Cancel response failed: {exc}")
            return

        if response.goals_canceling:
            self.get_logger().info("Cancel request accepted; waiting for final status.")
        else:
            self.get_logger().warning("Cancel request was not accepted.")

    def _result_callback(self, future: Any) -> None:
        try:
            wrapped_result = future.result()
            status = wrapped_result.status
            result_payload = wrapped_result.result
        except Exception as exc:
            self.get_logger().error(f"Result handling failed: {exc}")
            self._finish()
            return

        status_names = {
            GoalStatus.STATUS_UNKNOWN: "UNKNOWN",
            GoalStatus.STATUS_ACCEPTED: "ACCEPTED",
            GoalStatus.STATUS_EXECUTING: "EXECUTING",
            GoalStatus.STATUS_CANCELING: "CANCELING",
            GoalStatus.STATUS_SUCCEEDED: "SUCCEEDED",
            GoalStatus.STATUS_CANCELED: "CANCELED",
            GoalStatus.STATUS_ABORTED: "ABORTED",
        }
        status_name = status_names.get(status, str(status))
        self.get_logger().info(f"Final Action status: {status_name}")

        # Humble's result payload is empty. Newer interfaces may add error fields.
        error_code = getattr(result_payload, "error_code", None)
        error_msg = getattr(result_payload, "error_msg", "")
        if error_code not in (None, 0):
            self.get_logger().error(
                f"Action result error_code={error_code}, error_msg={error_msg!r}"
            )

        self._finish()

    def _finish(self) -> None:
        if self._cancel_timer is not None:
            self.destroy_timer(self._cancel_timer)
            self._cancel_timer = None
        self._done = True


def main(args: list[str] | None = None) -> None:
    """Run one configured NavigateToPose client node."""
    rclpy.init(args=args)
    node: NavigateToPoseClient | None = None
    try:
        node = NavigateToPoseClient()
        if node.send_configured_goal():
            while rclpy.ok() and not node.done:
                rclpy.spin_once(node, timeout_sec=0.1)
    except (TypeError, ValueError) as exc:
        if node is not None:
            node.get_logger().error(f"Invalid configuration: {exc}")
        else:
            print(f"Invalid configuration: {exc}")
    except KeyboardInterrupt:
        if node is not None:
            node.get_logger().warning("Interrupted by user.")
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
