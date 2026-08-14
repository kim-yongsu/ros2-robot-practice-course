---
title: 7. 이름보다 type·endpoint·QoS·실제 값을 본다
source_pdf_page: 11
canonical_language: ko
course_id: burger-v1
volume: 1
part: 2
lesson: 7
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="07" data-lesson-title="이름보다 type·endpoint·QoS·실제 값을 본다"></div>

<p class="lesson-kicker">PART 2 · ROS 2 통신과 실행 증거 / LESSON 07</p>

# 7. 이름보다 type·endpoint·QoS·실제 값을 본다

토픽 이름의 존재를 통신 증거로 확대하지 않고 endpoint type·QoS 호환성과 실제 message를 순서대로 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 11쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ROS 2 토픽을 이름에서 실제 값까지 조사하는 CLI 순서와 QoS 정책 질문을 정리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-08.png)

## 학습 목표

- 토픽 조사 순서를 list → endpoint → interface → value → rate로 실행한다.
- Reliability·Durability·History·Depth 질문을 실제 endpoint에 대조한다.
- 일반론으로 QoS를 바꾸지 않고 설치본 값을 근거로 판단한다.

## 선수 조건

- Lesson 06의 Topic 계약
- 조사할 `/scan` publisher 또는 해당 항목을 HOLD로 둘 준비

## 핵심 개념

| QoS 정책 | 질문 | 대표 값 |
| --- | --- | --- |
| Reliability | 손실을 허용하는가? | `best_effort` / `reliable` |
| Durability | 늦게 온 Subscriber가 과거 값을 받는가? | `volatile` / `transient_local` |
| History·Depth | 얼마나 많은 sample을 보관하는가? | `keep_last` / queue depth |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 topic list -t
ros2 topic info -v /scan
ros2 interface show sensor_msgs/msg/LaserScan
ros2 topic echo /scan --once
ros2 topic hz /scan
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- `/scan`의 type과 Publisher·Subscriber endpoint를 확인한다.
- 실제 message 한 건과 관찰 주기를 각각 확인한다.
- 실제 endpoint QoS를 비교한다.

## 관찰 포인트

- 이름은 있지만 publisher가 0인지, endpoint는 있으나 message가 없는지 구분한다.
- `ros2 topic hz` 관찰값을 장비 고정 성능으로 과장하지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
type·endpoint·QoS·실제 message가 조사 범위에서 서로 호환됨을 증거로 확인한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
토픽 또는 endpoint가 없거나 message 관찰이 아직 실행되지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
LiDAR는 보통 best effort라는 일반론만으로 QoS 설정을 임의 변경한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- `ros2 topic list`만 보고 통신 PASS
- type 확인 없이 echo 실패를 네트워크 문제로 단정
- publisher와 subscriber의 실제 QoS를 보지 않음

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `topic list -t`와 `topic info -v`
- [ ] interface 정의
- [ ] `echo --once`와 `hz` 관찰 기록

## 확인 문제

**질문:** `/scan` 이름이 존재하면 LiDAR message가 실제로 흐르는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
그렇다고 단정할 수 없다. endpoint·type·QoS와 실제 `echo` 또는 주기 관찰을 별도로 확인해야 한다.
:::

## 실습 과제

하나의 토픽에 대해 다섯 명령을 순서대로 실행하고 각 단계가 증명하는 것과 아직 증명하지 못한 것을 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 07 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 06 · Topic·Service·Action·Parameter를 선택한다](06-topic-service-action-parameter를-선택한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 08 · 실제 Humble 증거 — turtlesim과 rqt_graph](08-실제-humble-증거-turtlesim과-rqt_graph.md)
:::

::::
