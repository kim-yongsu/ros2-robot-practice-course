---
title: 문제 해결
canonical_language: ko
course_id: burger-v1
status: source-supported
---

# 문제 해결

무작위 튜닝 대신 **마지막 PASS와 첫 FAIL**을 찾는다.

## 첫 실패 사다리

1. 안전·전원
2. 장치·권한·firmware
3. OS·shell·ROS 환경
4. 네트워크·discovery
5. endpoint·type·QoS·message
6. TF·time·pose
7. Lifecycle·costmap·Action
8. OpenCR·motor·wheel

## 증상별 시작점

| 증상 | 마지막 PASS | 다음 확인 |
| --- | --- | --- |
| SSH도 안 됨 | 전원 | IP·Wi-Fi·SBC |
| Topic은 보이나 수신 0 | name·type | endpoint·QoS |
| Path 있음·command 없음 | Planner | Controller·local costmap |
| command 있음·wheel 정지 | ROS command | OpenCR·motor·wheel |

## 다시 시작하기

- [Lesson 10 · graph 발견 계층](chapters/10-ros-graph가-안-보이면-층을-나눈다.md)
- [Lesson 15 · bringup Gate](chapters/15-bringup은-일곱-게이트를-통과한-뒤-실행한다.md)
- [Lesson 20 · Nav2 Goal Gate](chapters/20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다.md)
- [Lesson 22 · 첫 실패 계층](chapters/22-문제는-처음-깨진-계층에서-자른다.md)
- [Lesson 24 · 회귀시험](chapters/24-한-변수만-바꾸고-같은-시험으로-회귀한다.md)

:::{danger}
정지 불가·발열·반복 disconnect가 있으면 진단 명령보다 먼저 STOP하고 전원을 차단한다.
:::
