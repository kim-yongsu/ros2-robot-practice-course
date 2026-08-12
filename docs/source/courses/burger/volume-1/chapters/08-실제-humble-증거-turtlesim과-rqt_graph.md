---
title: "8. 실제 Humble 증거 — turtlesim과 rqt_graph"
source_pdf_page: 12
canonical_language: ko
---

# 8. 실제 Humble 증거 — turtlesim과 rqt_graph

Ubuntu 22.04·ROS 2 Humble 실행 화면에서 Publisher → Topic → Subscriber 연결과 시뮬레이터의 상태 변화를 함께 확인한다.

![왼쪽 turtlesim의 이동 궤적과 teleop 터미널, 오른쪽 rqt_graph의 /teleop_turtle → /turtle1/cmd_vel → /turtlesim 연결](/_static/generated/diagrams/burger/volume-1/figure-09.png)

실제 turtlesim과 rqt_graph 실행 증거

| 관찰 | 증명하는 것 | 아직 증명하지 않는 것 |
| --- | --- | --- |
| 거북이 궤적 | 명령이 simulator 상태를 바꿈 | 실물 Burger motor |
| graph 연결 | Publisher·Topic·Subscriber 관계 | QoS·값의 정확성 |
| 4.446m Pose 변화 | 실행 전후 위치 변화 | 제어 정밀도 |

## 그림 바깥에서 다시 증명한다

```bash
ros2 node info /teleop_turtle
ros2 topic info -v /turtle1/cmd_vel
ros2 topic echo /turtle1/cmd_vel --once
```

중요  rqt_graph는 연결을 생성하지 않는다. 이미 존재하는 graph를 시각화할 뿐이다. 선이 없으면 실행 명령·Node 로그·endpoint부터 확인한다.
