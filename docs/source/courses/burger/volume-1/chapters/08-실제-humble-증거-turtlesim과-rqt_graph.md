---
title: 8. 실제 Humble 증거 — turtlesim과 rqt_graph
source_pdf_page: 12
canonical_language: ko
course_id: burger-v1
volume: 1
part: 2
lesson: 8
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="08" data-lesson-title="실제 Humble 증거 — turtlesim과 rqt_graph"></div>

<p class="lesson-kicker">PART 2 · ROS 2 통신과 실행 증거 / LESSON 08</p>

# 8. 실제 Humble 증거 — turtlesim과 rqt_graph

Publisher → Topic → Subscriber 연결과 simulator 상태 변화를 함께 보되 rqt_graph가 증명하지 못하는 범위를 남긴다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 12쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![turtlesim 궤적·rqt_graph 연결·Pose 변화가 증명하는 것과 증명하지 못하는 것을 비교한 증거 패널.](/_static/generated/diagrams/burger/volume-1/figure-09.png)

## 학습 목표

- 거북이 궤적, graph 연결, Pose 변화를 서로 다른 증거로 해석한다.
- rqt_graph가 연결을 생성하지 않고 기존 graph를 시각화함을 설명한다.
- graph 밖에서 Node·endpoint·message를 CLI로 재검증한다.

## 선수 조건

- Ubuntu 22.04·ROS 2 Humble 실행 환경
- turtlesim과 rqt_graph 실행 증거 또는 미실행 HOLD

## 핵심 개념

| 관찰 | 증명하는 것 | 아직 증명하지 않는 것 |
| --- | --- | --- |
| 거북이 궤적 | 명령이 simulator 상태를 바꿈 | 실물 Burger motor |
| graph 연결 | Publisher·Topic·Subscriber 관계 | QoS·값의 정확성 |
| 4.446 m Pose 변화 | 실행 전후 위치 변화 | 제어 정밀도 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 node info /teleop_turtle
ros2 topic info -v /turtle1/cmd_vel
ros2 topic echo /turtle1/cmd_vel --once
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 시각적 궤적과 graph 관계를 같은 실행 회차에서 확인한다.
- CLI로 `/teleop_turtle`과 `/turtle1/cmd_vel`을 재확인한다.

## 관찰 포인트

- graph 선이 없으면 rqt_graph 설정이 아니라 실행 명령·Node 로그·endpoint부터 본다.
- 4.446 m는 원본 실행 전후 Pose 변화이며 제어 정밀도 수치가 아니다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
그림의 세 관찰과 CLI 증거를 연결하고 실물 Burger까지 증명했다고 과장하지 않는다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
원본과 같은 실행 증거를 현재 환경에서 재현하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
rqt_graph 창이 열렸거나 선이 보였다는 이유만으로 QoS·값·실물 motor를 PASS한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- rqt_graph가 Node 연결을 만든다고 설명
- simulator 움직임을 실물 motor 증거로 전환
- Pose 변화량을 정밀도 수치로 오해

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] turtlesim 상태 변화 캡처
- [ ] rqt_graph 캡처
- [ ] Node·endpoint·message CLI 출력

## 확인 문제

**질문:** rqt_graph에 선이 없으면 rqt_graph가 연결을 만들도록 조작해야 하는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. rqt_graph는 기존 graph를 시각화할 뿐이므로 실행 명령·Node 로그·endpoint를 먼저 확인한다.
:::

## 실습 과제

turtlesim 실행 한 회차에서 화면, graph, CLI 세 증거를 모아 각각의 증명 범위를 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 08 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 07 · 이름보다 type·endpoint·QoS·실제 값을 본다](07-이름보다-type-endpoint-qos-실제-값을-본다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 09 · 실제 Humble 증거 — C++ talker와 Python listener](09-실제-humble-증거-c-talker와-python-listener.md)
:::

::::
