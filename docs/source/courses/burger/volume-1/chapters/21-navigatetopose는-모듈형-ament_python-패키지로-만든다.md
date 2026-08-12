---
title: "21. NavigateToPose는 모듈형 ament_python 패키지로 만든다"
source_pdf_page: 25
canonical_language: ko
---

# 21. NavigateToPose는 모듈형 ament_python 패키지로 만든다

ament_python 구조와 Goal response·Feedback·Result·Cancel Future를 분리해 Accepted를 성공으로 오판하지 않는다.

![metadata·install entry·source·test 구조와 Goal response, Feedback, terminal Result, Cancel·Future 오류를 분리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-22.png)

TREE-21-01 · ament_python 패키지 구조와 Goal·Feedback·Result·Cancel·Future 오류 경계를 분리한다.

| 상태·오류 | 정확한 뜻 | 종료 판정 |
| --- | --- | --- |
| SERVER_TIMEOUT | Action server 미발견 | Goal 미전송 |
| REJECTED | 서버가 Goal을 미수락 | 실패 종료 |
| ACCEPTED | 작업 시작 허가 | 아직 성공 아님 |
| terminal GoalStatus | SUCCEEDED / ABORTED / CANCELED | 각 결과 분리 |
| Future error | Goal / Result / Cancel 경계 예외 | 명시적 Outcome |

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 \
  burger_nav2_goal_client \
  --dependencies rclpy nav2_msgs action_msgs geometry_msgs \
  builtin_interfaces
colcon build --symlink-install --packages-select burger_nav2_goal_client
source install/setup.bash
ros2 interface show nav2_msgs/action/NavigateToPose
ros2 run burger_nav2_goal_client go_to_pose --ros-args \
  -p x:=1.0 -p y:=0.0 -p yaw:=0.0
```

주의  동반 패키지의 정적·순수 로직 시험과 Humble colcon·DDS·Nav2·실물 통합시험은 다른 검증층이다. Cancel은 물리 비상정지가 아니다.


## 공개 예제 source

:::{warning}
이 preview에는 단일 파일 교육 예제만 포함한다. 완전한 ROS package source는 실제 package tree, maintainer identity, license, Humble `colcon build/test` 증거가 함께 확인될 때 `ros2_ws/src`에 추가한다. 누락된 파일을 추정해 조립하지 않는다.
:::

아래 코드는 `examples/`의 실제 파일을 직접 포함한다.

```{literalinclude} ../../../../../../examples/burger/volume1/navigate_to_pose_client.py
:language: python
:linenos:
```
