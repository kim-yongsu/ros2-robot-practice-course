---
title: "11. PoseStamped는 frame·time·position·orientation 계약이다"
source_pdf_page: 15
canonical_language: ko
---

# 11. PoseStamped는 frame·time·position·orientation 계약이다

숫자만 읽지 말고 어느 좌표계에서 언제 측정한 위치와 회전인지 함께 확인한다.

![일반 로봇 frame과 camera optical frame의 축을 비교하고 PoseStamped의 frame_id, stamp, position, orientation을 분리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-12.png)

POSE-11-01 · frame과 stamp를 잃으면 position과 Quaternion도 해석할 수 없다.

| 필드 | 뜻 | 첫 검사 |
| --- | --- | --- |
| header.frame_id | 좌표값의 기준 frame | body·optical 축을 구분 |
| header.stamp | 측정 시각 | TF 시각과 호환되는지 확인 |
| position x·y·z | 해당 frame의 위치 | 단위와 축 방향 확인 |
| orientation x·y·z·w | Quaternion 회전 | z 하나를 yaw로 읽지 않음 |

핵심  평면 이동에서 roll=pitch=0일 때만 qz=sin(yaw/2), qw=cos(yaw/2)라는 단순식을 쓴다.

핵심  Yaw 0° → (qz,qw)=(0,1) · 90° → (0.7071,0.7071) · 180° → (1,0) · -90° → (-0.7071,0.7071)

핵심  세 값 구분: position.z는 현재 frame의 z축 위치다.

camera optical z는 카메라가 보는 전방 거리이며, orientation.z는 Quaternion의 qz 성분이다.
