---
title: "14. /cmd_vel과 실제 바퀴 사이의 경계를 나눈다"
source_pdf_page: 18
canonical_language: ko
---

# 14. /cmd_vel과 실제 바퀴 사이의 경계를 나눈다

명령 발행, SBC 수신, OpenCR 전달, 실제 wheel 반응을 서로 다른 증거로 확인한다.

![Remote PC의 cmd_vel이 SBC와 OpenCR을 거쳐 wheel로 가고 sensor 상태가 돌아오는 양방향 구조.](/_static/generated/diagrams/burger/volume-1/figure-15.png)

ARCH-14-01 · 명령 경로와 상태 경로는 양방향이지만, ROS 신호와 물리 동작은 같은 증거가 아니다.

| 증거 층 | PASS 기준 | 아직 증명하지 못한 것 |
| --- | --- | --- |
| Publisher | /cmd_vel publisher와 type 확인 | 값 변화·SBC 수신 |
| Message | Twist 값이 의도대로 변함 | OpenCR·wheel 반응 |
| Device 경계 | turtlebot3_node·port·log 정상 | motor torque·방향 |
| 물리 반응 | wheel 이동·즉시 정지 관찰 | 장기 안전성 |

```bash
# Remote PC
ros2 topic info /cmd_vel --verbose
ros2 topic echo /cmd_vel --once
ros2 topic list | grep -E 'battery_state|imu|joint_states|odom|scan'
```

주의  Humble teleop은 Twist를 사용한다. Jazzy의 TwistStamped 경로를 그대로 섞지 않는다.
