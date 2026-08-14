---
title: 1. Burger로 ROS 2의 공통 기준선을 만든다
source_pdf_page: 5
canonical_language: ko
course_id: burger-v1
volume: 1
part: 1
lesson: 1
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="01" data-lesson-title="Burger로 ROS 2의 공통 기준선을 만든다"></div>

<p class="lesson-kicker">PART 1 · 환경 기준선 / LESSON 01</p>

# 1. Burger로 ROS 2의 공통 기준선을 만든다

TurtleBot3 Burger를 환경·통신·좌표·실물·자율주행·유지보수 계약을 한 번에 확인하는 기준 플랫폼으로 사용한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 5쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Burger 1권의 독자별 학습 목표와 Graph·실물·Nav2 종료 Gate를 비교한 도해.](/_static/generated/diagrams/burger/volume-1/figure-02.png)

## 학습 목표

- Burger 1권의 전체 학습 경로와 독자별 완료 기준을 설명한다.
- GUI·이름의 존재와 실제 값·물리 반응·최종 상태·증거를 구분한다.
- PASS와 HOLD의 경계를 다음 단계 입력으로 기록한다.

## 선수 조건

- 이 Lesson이 1권의 시작점이다.
- 실물 시험 전 물리 정지와 전원 차단 수단을 확보한다.

## 핵심 개념

| 독자 | 이 책으로 할 수 있어야 하는 일 |
| --- | --- |
| 학생 | 명령을 따라 하고 정상 결과·STOP 조건·첫 진단을 설명 |
| 교사 | 실습 순서와 실패 주입 지점을 통제 |
| 신입 | 환경·graph·TF·하드웨어·Nav2 계층을 분리 진단 |
| 베테랑 | 명령·interface·증거 위치를 빠르게 재확인 |

| 종료 Gate | PASS 증거 | HOLD 경계 |
| --- | --- | --- |
| Graph·TF | type·endpoint·TF chain | 이름만 존재 |
| 실물·지도 | 정지·scan·odom·map 파일 | simulator만 확인 |
| Nav2·진단 | Result·실패 재현·복구 기록 | Goal 전송만 확인 |

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

- 6개 PART가 하나의 Burger 기준선으로 이어짐을 이해한다.
- 앞 단계의 정상 결과와 evidence 경로가 다음 단계 입력임을 확인한다.

## 관찰 포인트

- 현재 단계에서 실제로 확보한 증거와 아직 없는 입력을 분리한다.
- 화면이 열리거나 이름이 보였다는 사실만으로 PASS하지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
학습 경로, 판정 원칙, 각 Gate의 증거와 HOLD 경계를 자신의 말로 설명한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
실물·지도·Nav2 결과가 아직 실행되지 않았거나 증거가 없으면 해당 항목을 HOLD로 남긴다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
GUI·토픽 이름·Goal 전송만으로 실물 또는 Nav2 성공을 선언한다.
:::

::::

## STOP 조건

:::{danger}
정지 불가·발열·반복 disconnect·원인 미확인 상태에서는 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- Burger를 학습 목적 그 자체로만 보고 공통 ROS 2 기준선 역할을 놓침
- 검사 범위를 밝히지 않은 채 PASS를 확대 해석함

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 현재 환경과 학습 시작 상태 기록
- [ ] 각 Gate별 실제 증거 또는 HOLD 사유
- [ ] 다음 Lesson으로 넘어가는 근거

## 확인 문제

**질문:** 토픽 이름이 보이면 통신과 실물 반응이 모두 PASS인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. type·endpoint·실제 message와 필요한 경우 물리 반응·최종 상태·증거까지 별도로 확인해야 한다.
:::

## 실습 과제

현재 가지고 있는 Burger·Remote PC·SBC 증거를 Graph·TF / 실물·지도 / Nav2·진단 세 줄로 나누고 PASS 또는 HOLD 사유를 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 01 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[1권 시작하기](../start.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 02 · 터미널·Linux 생존선을 먼저 확보한다](02-터미널-linux-생존선을-먼저-확보한다.md)
:::

::::
