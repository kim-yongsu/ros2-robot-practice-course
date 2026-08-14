---
title: 13. URDF와 robot_state_publisher의 책임을 나눈다
source_pdf_page: 17
canonical_language: ko
course_id: burger-v1
volume: 1
part: 3
lesson: 13
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="13" data-lesson-title="URDF와 robot_state_publisher의 책임을 나눈다"></div>

<p class="lesson-kicker">PART 3 · 발견·좌표·TF·URDF / LESSON 13</p>

# 13. URDF와 robot_state_publisher의 책임을 나눈다

모델 정의, joint 상태 입력, TF 발행, RViz 시각화를 하나의 프로그램 책임으로 섞지 않는다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 17쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![URDF visual·collision·inertial·joint와 robot_state_publisher·joint_states·TF 책임을 분리한 흐름도.](/_static/generated/diagrams/burger/volume-1/figure-14.png)

## 학습 목표

- URDF의 visual·collision·inertial·joint 책임을 구분한다.
- robot_state_publisher의 Node·parameter·TF endpoint를 확인한다.
- joint_state_publisher GUI와 실물 encoder·OpenCR 증거의 경계를 설명한다.

## 선수 조건

- Lesson 12의 TF edge·authority 이해
- robot_state_publisher 실행 또는 미실행 HOLD

## 핵심 개념

| URDF 요소 | 책임 | 주의 |
| --- | --- | --- |
| visual | 화면에 보이는 형상 | collision 형상과 다를 수 있음 |
| collision | 물리·충돌 형상 | 단순하고 닫힌 형상을 우선 |
| inertial | 질량·관성 | simulation 안정성에 영향 |
| joint | link 관계와 운동 | 축·limit·parent·child 확인 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 node info /robot_state_publisher
ros2 param get /robot_state_publisher robot_description
ros2 topic info --verbose /joint_states
ros2 topic echo /joint_states --once
ros2 topic info --verbose /tf
ros2 topic info --verbose /tf_static
ros2 run tf2_tools view_frames
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- robot_description parameter와 joint_states 입력을 분리해 확인한다.
- `/tf`와 `/tf_static` endpoint와 TF tree를 확인한다.

## 관찰 포인트

- visual과 collision이 같은 형상이라고 가정하지 않는다.
- GUI로 만든 joint state가 실물 encoder 증거를 대신하지 않음을 표시한다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
URDF 요소·joint 상태 입력·TF authority·시각화 책임을 서로 다른 증거로 설명한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
robot_description 또는 joint_states·TF endpoint 중 필요한 증거가 없다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
RViz에 모델이 보인다는 사실을 collision·inertial·실물 encoder PASS로 확대한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- visual mesh만 보고 collision 정상 판정
- joint_state_publisher GUI를 실물 OpenCR 증거로 사용
- TF publisher를 URDF 파일 자체라고 설명

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] robot_description 조회
- [ ] joint_states endpoint와 message
- [ ] `/tf`·`/tf_static` endpoint 및 TF tree

## 확인 문제

**질문:** RViz에서 joint가 움직이면 실물 encoder와 OpenCR이 정상인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. joint_state_publisher GUI는 모델 시험용 입력이며 실물 encoder·OpenCR 증거를 대신하지 않는다.
:::

## 실습 과제

한 URDF link/joint를 골라 visual·collision·inertial·joint와 runtime publisher의 책임을 각각 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 13 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 12 · TF edge마다 authority와 시간을 확인한다](12-tf-edge마다-authority와-시간을-확인한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 14 · /cmd_vel과 실제 바퀴 사이의 경계를 나눈다](14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다.md)
:::

::::
