---
title: 14. /cmd_vel과 실제 바퀴 사이의 경계를 나눈다
source_pdf_page: 18
canonical_language: ko
course_id: burger-v1
volume: 1
part: 4
lesson: 14
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="14" data-lesson-title="/cmd_vel과 실제 바퀴 사이의 경계를 나눈다"></div>

<p class="lesson-kicker">PART 4 · 실물 명령과 시뮬레이션 / LESSON 14</p>

# 14. /cmd_vel과 실제 바퀴 사이의 경계를 나눈다

명령 발행, SBC 수신, OpenCR 전달, 실제 wheel 반응을 서로 다른 증거층으로 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 18쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ROS /cmd_vel publisher에서 SBC·OpenCR·실제 wheel로 이어지는 명령 경로와 증거 경계를 분리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-15.png)

## 학습 목표

- Publisher·Message·Device·물리 반응의 증거를 분리한다.
- `/cmd_vel` type과 실제 값, 상태 토픽을 조사한다.
- Humble Twist와 Jazzy TwistStamped 경로를 혼합하지 않는다.

## 선수 조건

- PART 3의 graph·TF·URDF 기준선
- 실물 시험 전 안전·전원 차단 수단

## 핵심 개념

| 증거 층 | PASS 기준 | 아직 증명하지 못한 것 |
| --- | --- | --- |
| Publisher | `/cmd_vel` publisher와 type 확인 | 값 변화·SBC 수신 |
| Message | Twist 값이 의도대로 변함 | OpenCR·wheel 반응 |
| Device 경계 | `turtlebot3_node`·port·log 정상 | motor torque·방향 |
| 물리 반응 | wheel 이동·즉시 정지 관찰 | 장기 안전성 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 topic info /cmd_vel --verbose
ros2 topic echo /cmd_vel --once
ros2 topic list | grep -E 'battery_state|imu|joint_states|odom|scan'
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 현재 설치본의 `/cmd_vel` publisher·type을 확인한다.
- 의도한 Twist 값과 필요한 상태 토픽의 존재를 조사한다.
- 실물 wheel 이동·정지는 별도 물리 관찰로 남긴다.

## 관찰 포인트

- ROS 신호와 물리 동작이 같은 증거가 아님을 유지한다.
- Humble teleop의 Twist 계약에 Jazzy TwistStamped 명령을 섞지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
Publisher·message·device·물리 반응 네 층이 각각 필요한 증거로 확인된다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
ROS message까지만 확인했고 OpenCR 또는 wheel 반응은 아직 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
`/cmd_vel` 이름이 보인다는 이유로 motor·wheel·정지까지 PASS한다.
:::

::::

## STOP 조건

:::{danger}
정지 불가·예상 밖 방향·발열·반복 disconnect가 있으면 즉시 전원을 차단하고 다음 단계로 가지 않는다.
:::

## 실패·문제해결

- topic 이름과 실제 수신을 같은 증거로 기록
- device log 없이 port를 영구값으로 고정
- Jazzy 명령을 Humble 과정에 병합

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `topic info --verbose`와 `echo --once`
- [ ] turtlebot3_node·device log
- [ ] wheel 이동·즉시 정지 관찰표

## 확인 문제

**질문:** `/cmd_vel` 값이 보이면 실제 wheel 반응도 증명되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. OpenCR 전달과 실제 wheel 이동·정지는 별도 device·물리 증거로 확인해야 한다.
:::

## 실습 과제

한 번의 짧은 명령을 Publisher·Message·Device·물리 반응 네 줄로 나눠 증거와 HOLD를 기록한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 14 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 13 · URDF와 robot_state_publisher의 책임을 나눈다](13-urdf와-robot_state_publisher의-책임을-나눈다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 15 · bringup은 일곱 게이트를 통과한 뒤 실행한다](15-bringup은-일곱-게이트를-통과한-뒤-실행한다.md)
:::

::::
