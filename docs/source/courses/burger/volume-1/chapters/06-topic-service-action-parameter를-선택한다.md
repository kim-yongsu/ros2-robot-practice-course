---
title: 6. Topic·Service·Action·Parameter를 선택한다
source_pdf_page: 10
canonical_language: ko
course_id: burger-v1
volume: 1
part: 2
lesson: 6
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="06" data-lesson-title="Topic·Service·Action·Parameter를 선택한다"></div>

<p class="lesson-kicker">PART 2 · ROS 2 통신과 실행 증거 / LESSON 06</p>

# 6. Topic·Service·Action·Parameter를 선택한다

데이터 빈도만이 아니라 응답, 진행 상태, 취소, 설정 소유권을 기준으로 ROS 2 interface를 선택한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 10쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ROS 2 Topic·Service·Action·Parameter의 계약과 Burger 예, Action 단계별 실패를 비교한 도해.](/_static/generated/diagrams/burger/volume-1/figure-07.png)

## 학습 목표

- Topic·Service·Action·Parameter의 계약을 구분한다.
- NavigateToPose를 Goal·Feedback·Result·Cancel 단계로 나눈다.
- Action의 서버 발견, Goal 수락, 실행, 종료 실패를 분리한다.

## 선수 조건

- Lesson 05의 Node와 실행 단위 구분

## 핵심 개념

| 방식 | 계약 | Burger 예 |
| --- | --- | --- |
| Topic | Publisher·Subscriber의 비동기 message 교환 | `/scan` · `/odom` · `/cmd_vel` |
| Service | 한 request에 한 response | 상태 조회·짧은 명령 |
| Action | Goal·Feedback·Result·Cancel | NavigateToPose |
| Parameter | Node가 소유하는 실행 설정 | 속도·frame·plugin |

| Action 단계 | 클라이언트가 보는 것 | 서로 다른 실패 |
| --- | --- | --- |
| 서버 발견 | `wait_for_server` timeout | Server not found |
| Goal 응답 | accepted 여부 | Rejected |
| 실행 | Feedback·Cancel | 진행·취소 |
| 종료 | Result status | Succeeded·Aborted·Canceled |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

이 Lesson은 비교·판정 중심이다. 아래 표와 관찰 항목을 자신의 실행 기록에 적용한다.

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 작업 계약에 따라 interface를 선택하고 선택 이유를 설명한다.
- Action에서 Accepted와 terminal Result를 같은 성공으로 취급하지 않는다.

## 관찰 포인트

- Topic은 주기적 발행뿐 아니라 사건 기반 발행도 가능하다는 원문 경계를 유지한다.
- 장시간 실행·진행 확인·취소가 필요한지 먼저 본다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
주어진 작업을 네 interface 중 하나로 분류하고 서버 발견부터 종료까지 Action 상태를 분리한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
작업의 응답·진행·취소 요구가 정해지지 않아 interface를 선택할 수 없다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
Goal이 Accepted됐다는 사실을 작업 성공으로 기록한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- 데이터가 계속 흐른다는 이유 하나로 Topic 선택
- Service에 장시간 진행·취소 계약을 억지로 넣음
- Parameter를 독립 message stream처럼 설명

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 작업 요구와 선택한 interface의 대응표
- [ ] Action이면 server/accepted/feedback/result/cancel 상태 기록

## 확인 문제

**질문:** Action Goal이 Accepted되면 작업은 성공한 것인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. Accepted는 실행 시작 허가이며 terminal Result의 SUCCEEDED·ABORTED·CANCELED를 별도로 확인해야 한다.
:::

## 실습 과제

Burger 작업 세 개를 골라 Topic·Service·Action·Parameter 중 무엇을 쓸지 정하고 응답·진행·취소 요구를 근거로 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 06 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 05 · Package·Executable·Process·Node를 구분한다](05-package-executable-process-node를-구분한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 07 · 이름보다 type·endpoint·QoS·실제 값을 본다](07-이름보다-type-endpoint-qos-실제-값을-본다.md)
:::

::::
