---
title: "23. Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다"
source_pdf_page: 27
canonical_language: ko
---

# 23. Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다

환경·ROS 메시지·물리 관찰을 분리하고, 같은 실행의 명령·시간·파일 hash로 다시 재현할 수 있게 보존한다.

![환경과 명령, ROS 메시지와 파일, 실제 움직임과 안전 관찰을 분리하고 timestamp·명령·SHA-256으로 같은 실행에 연결하는 증거 묶음.](/_static/generated/diagrams/burger/volume-1/figure-24.png)

PACK-23-01 · 환경·ROS·물리 증거는 서로 보완하지만 서로를 대신하지 않으며 RUN_ID로 연결한다.

| 도구·자료 | 증명하는 것 | 증명하지 못하는 것 |
| --- | --- | --- |
| ros2 doctor | 환경·설정 snapshot | 실물 주행 성공 |
| topic info·hz | endpoint·QoS·관찰 주기 | 물리 반응 |
| rosbag2 | ROS message·timestamp | 정지 거리·충돌 부재 |
| 영상·관찰표 | 실제 움직임·안전 | graph·코드 상태 |

```bash
RUN_ID=$(date +%Y%m%d_%H%M%S)_burger_nav
EVIDENCE="$HOME/tb3_evidence/$RUN_ID"; mkdir -p "$EVIDENCE"
ros2 doctor --report > "$EVIDENCE/ros2_doctor.txt"
ros2 bag record -o "$EVIDENCE/runtime_bag" /scan /odom /tf /tf_static /cmd_vel
ros2 bag info "$EVIDENCE/runtime_bag" > "$EVIDENCE/bag_info.txt"
```

주의  command topic이 포함된 bag을 실물과 같은 Domain에서 바로 replay하지 않는다. bag은 ROS 메시지 증거이지 물리 안전 증거가 아니다.
