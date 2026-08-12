---
title: "12. TF edge마다 authority와 시간을 확인한다"
source_pdf_page: 16
canonical_language: ko
---

# 12. TF edge마다 authority와 시간을 확인한다

frame 이름만 보지 말고 누가 그 변환을 발행하며 어느 시각의 관계인지 확인한다.

![map, odom, base_link, base_scan의 TF tree와 각 edge의 일반적인 authority, timestamp 오류 진단을 보여 주는 도해.](/_static/generated/diagrams/burger/volume-1/figure-13.png)

TREE-12-01 · TurtleBot3 Burger의 LiDAR frame은 Humble URDF 기준 base_scan이다.

| TF edge | 일반적인 authority | 특성 |
| --- | --- | --- |
| map → odom | Localization 또는 SLAM | 전역 보정·점프 가능 |
| odom → base_link | Odometry source | 연속적이지만 drift 가능 |
| base_link → base_scan | URDF·robot_state_publisher | Burger의 고정 센서 관계 |

```bash
ros2 run tf2_ros tf2_echo map base_link
ros2 run tf2_ros tf2_echo base_link base_scan
ros2 run tf2_ros tf2_monitor map base_link
ros2 run tf2_tools view_frames
```

주의  frame이 없으면 연결·이름을 보고, Extrapolation이면 stamp·시계 동기화·지연을 본다.
