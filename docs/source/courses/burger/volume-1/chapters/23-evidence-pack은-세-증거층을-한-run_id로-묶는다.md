---
title: 23. Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다
source_pdf_page: 27
canonical_language: ko
course_id: burger-v1
volume: 1
part: 6
lesson: 23
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="23" data-lesson-title="Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다"></div>

<p class="lesson-kicker">PART 6 · 진단·증거·회귀·프로젝트 / LESSON 23</p>

# 23. Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다

환경·ROS message·물리 관찰을 분리하고 명령·시간·파일 hash로 같은 실행을 재현할 수 있게 보존한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 27쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ros2 doctor·topic·rosbag·영상 증거를 하나의 RUN_ID로 연결하고 서로의 한계를 구분한 도해.](/_static/generated/diagrams/burger/volume-1/figure-24.png)

## 학습 목표

- 환경·ROS·물리 증거가 서로 대신하지 못함을 설명한다.
- RUN_ID로 doctor·rosbag·관찰 자료를 같은 실행에 연결한다.
- command topic이 든 bag의 실물 replay 위험을 구분한다.

## 선수 조건

- Lesson 22의 첫 FAIL 기록
- 증거를 저장할 경로와 충분한 저장 공간

## 핵심 개념

| 도구·자료 | 증명하는 것 | 증명하지 못하는 것 |
| --- | --- | --- |
| `ros2 doctor` | 환경·설정 snapshot | 실물 주행 성공 |
| `topic info`·`hz` | endpoint·QoS·관찰 주기 | 물리 반응 |
| rosbag2 | ROS message·timestamp | 정지 거리·충돌 부재 |
| 영상·관찰표 | 실제 움직임·안전 | graph·코드 상태 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
RUN_ID=$(date +%Y%m%d_%H%M%S)_burger_nav
EVIDENCE="$HOME/tb3_evidence/$RUN_ID"; mkdir -p "$EVIDENCE"
ros2 doctor --report > "$EVIDENCE/ros2_doctor.txt"
ros2 bag record -o "$EVIDENCE/runtime_bag" /scan /odom /tf /tf_static /cmd_vel
ros2 bag info "$EVIDENCE/runtime_bag" > "$EVIDENCE/bag_info.txt"
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 한 RUN_ID 아래 환경 snapshot·bag·bag info·물리 관찰을 모은다.
- 각 자료가 증명하는 범위와 못하는 범위를 함께 기록한다.

## 관찰 포인트

- 명령·시간·파일 hash가 같은 실행을 가리키는지 확인한다.
- bag replay가 원래 실행과 같은 안전 조건을 자동 보장하지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
세 증거층이 RUN_ID로 연결되고 각 자료의 한계가 명시된다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
환경·ROS·물리 중 한 층이 없거나 실행 시각·명령·hash 연결이 없다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
command topic이 포함된 bag을 실물과 같은 Domain에서 바로 replay한다.
:::

::::

## STOP 조건

:::{danger}
command topic이 든 bag을 실물과 같은 Domain에서 곧바로 replay하지 않는다.
:::

## 실패·문제해결

- 영상 하나로 graph·QoS·코드 상태까지 증명
- bag만 저장하고 환경·명령 누락
- 서로 다른 실행의 파일을 같은 RUN_ID에 혼합

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] RUN_ID와 실행 명령
- [ ] `ros2_doctor.txt`·`runtime_bag`·`bag_info.txt`
- [ ] 물리 관찰표·영상·파일 hash

## 확인 문제

**질문:** rosbag에 `/cmd_vel`이 기록됐으면 실물 정지 거리도 증명되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. bag은 ROS message·timestamp 증거이며 정지 거리·충돌 부재는 물리 관찰이 필요하다.
:::

## 실습 과제

한 실행의 Evidence Pack 폴더를 만들고 각 파일 옆에 증명 범위와 증명하지 못하는 범위를 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 23 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 22 · 문제는 처음 깨진 계층에서 자른다](22-문제는-처음-깨진-계층에서-자른다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 24 · 한 변수만 바꾸고 같은 시험으로 회귀한다](24-한-변수만-바꾸고-같은-시험으로-회귀한다.md)
:::

::::
