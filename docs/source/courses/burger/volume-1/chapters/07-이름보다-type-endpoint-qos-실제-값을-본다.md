---
title: "7. 이름보다 type·endpoint·QoS·실제 값을 본다"
source_pdf_page: 11
canonical_language: ko
---

# 7. 이름보다 type·endpoint·QoS·실제 값을 본다

토픽 이름이 존재하는 것만으로 통신이 증명되지는 않는다. Publisher와 Subscriber의 type과 QoS가 호환되고 실제 message가 흘러야 한다.

![토픽 이름과 type, endpoint, interface, 실제 값, 주기와 QoS를 차례로 확인하는 다섯 단계 사다리](/_static/generated/diagrams/burger/volume-1/figure-08.png)

ROS 2 CLI 조사 순서

```bash
ros2 topic list -t
ros2 topic info -v /scan
ros2 interface show sensor_msgs/msg/LaserScan
ros2 topic echo /scan --once
ros2 topic hz /scan
```

| QoS 정책 | 질문 | 대표 값 |
| --- | --- | --- |
| Reliability | 손실을 허용하는가? | best_effort / reliable |
| Durability | 늦게 온 구독자가 과거 값을 받는가? | volatile / transient_local |
| History·Depth | 얼마나 많은 sample을 보관하는가? | keep_last / queue depth |

센서 진단  LiDAR topic이 best effort일 수 있다는 일반론으로 값을 바꾸지 않는다. ros2 topic info -v에서 실제 endpoint QoS를 대조한다.
