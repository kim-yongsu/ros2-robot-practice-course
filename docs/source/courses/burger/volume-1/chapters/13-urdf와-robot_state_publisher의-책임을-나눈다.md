---
title: "13. URDF와 robot_state_publisher의 책임을 나눈다"
source_pdf_page: 17
canonical_language: ko
---

# 13. URDF와 robot_state_publisher의 책임을 나눈다

모델 정의, joint 상태, TF 발행, RViz 시각화를 한 프로그램의 책임처럼 섞지 않는다.

![Xacro와 URDF가 robot_description이 되고 robot_state_publisher가 joint_states를 받아 tf와 tf_static을 발행해 RViz가 시각화하는 흐름.](/_static/generated/diagrams/burger/volume-1/figure-14.png)

FLOW-13-01 · 모델, 상태 입력, TF authority, 시각화는 서로 다른 책임이다.

| URDF 요소 | 책임 | 주의 |
| --- | --- | --- |
| visual | 화면에 보이는 형상 | collision 형상과 다를 수 있음 |
| collision | 물리·충돌 형상 | 단순하고 닫힌 형상을 우선 |
| inertial | 질량·관성 | 시뮬레이션 안정성에 영향 |
| joint | link 관계와 운동 | 축·limit·parent·child 확인 |

```bash
ros2 node info /robot_state_publisher
ros2 param get /robot_state_publisher robot_description
ros2 topic info --verbose /joint_states
ros2 topic echo /joint_states --once
ros2 topic info --verbose /tf
ros2 topic info --verbose /tf_static
ros2 run tf2_tools view_frames
```

주의  joint_state_publisher GUI는 모델 시험용 입력이다. 실물 encoder·OpenCR 증거를 대신하지 않는다.
