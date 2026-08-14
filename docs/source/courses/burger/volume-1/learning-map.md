---
title: 6단계 학습 지도
canonical_language: ko
course_id: burger-v1
status: source-supported
---

# 6단계 학습 지도

| PART | 제목 | Lesson | 완료 능력 |
| --- | --- | --- | --- |
| 1 | 환경 기준선 | 01–04 | OS · ROS · shell · workspace 기준선을 기록하고 같은 환경을 다시 복구한다. |
| 2 | ROS 2 통신과 실행 증거 | 05–09 | Package부터 Node까지의 실행 관계와 Topic·Service·Action·Parameter의 계약을 증거로 설명한다. |
| 3 | 발견·좌표·TF·URDF | 10–13 | ROS graph, PoseStamped, TF edge, robot_state_publisher를 서로 다른 진단층으로 읽는다. |
| 4 | 실물 명령과 시뮬레이션 | 14–17 | 실물 주행 전 Gate와 STOP을 확인하고 simulation과 실물 증거를 혼동하지 않는다. |
| 5 | SLAM·Localization·Nav2 | 18–21 | 지도·현재 위치·Goal 상태·Cancel을 분리하고 source-supported 기준으로 판정한다. |
| 6 | 진단·증거·회귀·프로젝트 | 22–25 | 실패·수정·rollback·증거·인수인계를 같은 실행 조건으로 재현한다. |

## 단계 연결

```text
환경 기준선
→ 통신과 실행 증거
→ 발견·좌표·TF·URDF
→ 실물 명령과 simulation
→ SLAM·Localization·Nav2
→ 진단·증거·회귀·프로젝트
```

각 화살표는 이전 PART의 **실제 PASS 또는 명시된 HOLD**가 다음 PART 입력으로 전달된다는 뜻이다.

## PART 바로가기

- [PART 1 · 환경 기준선](part-01-environment/index.md)
- [PART 2 · ROS 2 통신과 실행 증거](part-02-communication/index.md)
- [PART 3 · 발견·좌표·TF·URDF](part-03-frames/index.md)
- [PART 4 · 실물 명령과 시뮬레이션](part-04-hardware-sim/index.md)
- [PART 5 · SLAM·Localization·Nav2](part-05-navigation/index.md)
- [PART 6 · 진단·증거·회귀·프로젝트](part-06-evidence/index.md)
