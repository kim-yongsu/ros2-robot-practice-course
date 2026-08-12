---
title: "20. Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다"
source_pdf_page: 24
canonical_language: ko
---

# 20. Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다

BT Navigator가 planner·controller·behavior를 조정하며, 관련 managed node가 active가 아니면 첫 게이트에서 멈춘다.

![Lifecycle, TF·Pose, global/local costmap, Action·command ownership을 독립 게이트로 확인한 뒤 BT Navigator와 server 책임을 따라가는 구조.](/_static/generated/diagrams/burger/volume-1/figure-21.png)

GATE-20-01 · Lifecycle·TF/Pose·global/local costmap·Action/command ownership을 독립 게이트로 확인한다.

| 게이트 | PASS 기준 | FAIL 시 우선 확인 |
| --- | --- | --- |
| Lifecycle | 관련 server active | configure·activate·bond |
| TF·Pose | map→odom→base와 current pose 안정 | Localization·시간 |
| Costmaps | global map·footprint·layer / local sensor·obstacle update | Planner·Controller·sensor source |
| Action·command·STOP | server·publisher ownership·정지 수단 준비 | 중복 publisher·topic type |

```bash
ros2 lifecycle nodes
ros2 lifecycle get /planner_server
ros2 lifecycle get /controller_server
ros2 action info /navigate_to_pose
ros2 param dump /global_costmap/global_costmap
ros2 param dump /local_costmap/local_costmap
```

주의  node 이름·plugin·cmd_vel type은 설치본에서 탐지한다. Path 생성은 command·base motion·Goal 성공의 증거가 아니다.
