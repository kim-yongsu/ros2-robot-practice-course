---
title: "19. Initial Pose는 scan-map 정합으로 판정한다"
source_pdf_page: 23
canonical_language: ko
---

# 19. Initial Pose는 scan-map 정합으로 판정한다

로봇 아이콘을 옮긴 뒤 AMCL의 scan 점이 저장 지도 벽과 위치·yaw 모두 맞는지 확인한다.

![저장 지도와 scan·odom·TF 입력에 Initial Pose를 주고 AMCL의 map→odom 및 scan-map 정합을 확인하는 흐름.](/_static/generated/diagrams/burger/volume-1/figure-20.png)

ALIGN-19-01 · Initial Pose는 map origin 선언이 아니라 AMCL의 시작 가설이며, scan-map 정합이 실제 증거다.

| 관찰 | 정확한 뜻 | 다음 행동 |
| --- | --- | --- |
| Initial Pose | AMCL particle의 시작 위치·yaw | 실제 위치에 맞게 지정 |
| 아이콘 위치 | RViz 표시 | scan과 벽을 함께 확인 |
| scan 평행 이동 | x·y 오차 가능 | 위치를 다시 지정 |
| scan 회전 오차 | yaw 오차 가능 | 방향을 다시 지정 |
| 짧은 teleop | belief 수렴 보조 | Ctrl+C 후 Goal 준비 |

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:="$HOME/maps/classroom_v1.yaml"
# RViz: 2D Pose Estimate → scan-map 정합
ros2 run tf2_ros tf2_echo map base_link
ros2 topic info /cmd_vel --verbose
```

주의  teleop publisher를 남긴 채 Goal을 보내지 않는다. Initial Pose ≠ map origin, 로봇 아이콘 ≠ localization proof다.
