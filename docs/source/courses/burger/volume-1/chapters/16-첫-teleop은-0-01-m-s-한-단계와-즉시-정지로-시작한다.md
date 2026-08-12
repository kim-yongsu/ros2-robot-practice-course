---
title: "16. 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다"
source_pdf_page: 20
canonical_language: ko
---

# 16. 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다

최대 속도를 시험하지 말고, 입력·정지·publisher 종료·물리 정지를 짧은 폐루프로 확인한다.

![bringup, stop key 확인, 0.01 m/s 전진, 정지, 좌우 회전, 종료와 물리 정지 확인의 흐름.](/_static/generated/diagrams/burger/volume-1/figure-17.png)

FLOW-16-01 · first run은 한 단계 이동과 즉시 stop으로 닫으며 software stop을 E-stop으로 부르지 않는다.

| 단계 | 행동 | 증거 |
| --- | --- | --- |
| 준비 | bringup 유지·바닥 확보·정지 담당 | 주행 반경과 전원 차단 |
| 전진 | w 한 번 → 짧게 관찰 | target +0.01 m/s |
| 정지 | space 또는 s | 0 command + 실제 wheel 정지 |
| 회전 | a·d 한 단계씩 후 즉시 stop | 좌·우 방향·부호 |
| 종료 | Ctrl+C | publisher 제거·wheel 정지 재확인 |

```bash
# Remote PC
export TURTLEBOT3_MODEL=burger
ros2 run turtlebot3_teleop teleop_keyboard
# 다른 terminal
ros2 topic info /cmd_vel --verbose
```

주의  Burger 최대 0.22 m/s는 source 제한값이지 첫 시험 목표가 아니다. table 위 시험과 무감시 시험은 NO-GO다.
