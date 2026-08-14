---
title: 9. 실제 Humble 증거 — C++ talker와 Python listener
source_pdf_page: 13
canonical_language: ko
course_id: burger-v1
volume: 1
part: 2
lesson: 9
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="09" data-lesson-title="실제 Humble 증거 — C++ talker와 Python listener"></div>

<p class="lesson-kicker">PART 2 · ROS 2 통신과 실행 증거 / LESSON 09</p>

# 9. 실제 Humble 증거 — C++ talker와 Python listener

서로 다른 구현 언어가 같은 interface contract로 통신한 원본 로그의 sequence와 timestamp를 짝지어 검증한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 13쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![C++ talker와 Python listener의 7개 sequence·timestamp 대응과 원본 로그·증거 패널·SHA 역할을 정리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-10.png)

## 학습 목표

- C++ talker와 Python listener의 sequence 대응을 확인한다.
- timestamp 순서와 관찰 지연을 원본 7 sample 범위에서 해석한다.
- raw log·교육용 패널·환경·명령·SHA의 역할을 구분한다.

## 선수 조건

- Lesson 05~07의 Node·interface·message 조사
- 원본 로그 또는 공개 evidence 접근

## 핵심 개념

| 검사 | 결과 | 판정 |
| --- | --- | --- |
| sequence 대응 | 1~7 전부 일치 | message 전달 PASS |
| 시간 순서 | 모든 수신이 발행 뒤 | timestamp order PASS |
| 최대 관찰 지연 | 6.725 ms | 이 7 sample의 관찰값 |

| 파일 | 역할 | 보존 이유 |
| --- | --- | --- |
| 원본 log | 기계 판독 가능한 사실 | sequence 재검증 |
| 증거 패널 | 사람이 빠르게 이해 | 교육·리뷰 |
| 환경·명령·SHA | 실행 계보 | 재현·변조 확인 |

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

- sequence 1~7이 발행·수신 로그에서 모두 대응한다.
- 각 수신 timestamp가 대응 발행 뒤에 위치한다.
- 6.725 ms는 오직 이 7 sample의 최대 관찰값으로 기록한다.

## 관찰 포인트

- 증거 패널을 raw GUI screenshot으로 소개하지 않는다.
- 작은 sample 관찰값을 시스템 보장 성능으로 확대하지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
원본 로그로 sequence와 timestamp를 재검증하고 시각 패널의 출처 경계를 설명한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
원본 로그가 없거나 현재 실행에서 동일 검사를 수행하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
교육용 재배치 그림을 raw screenshot으로 가장하거나 6.725 ms를 일반 성능 보장으로 주장한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- 언어가 다르다는 이유로 interface 호환을 추정만 함
- 수신 로그만 보고 발행 sequence와 짝짓지 않음
- SHA·환경·명령을 제외한 이미지 하나만 보존

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] talker와 listener 원본 log
- [ ] sequence·timestamp 대응표
- [ ] 실행 환경·명령·파일 SHA

## 확인 문제

**질문:** 6.725 ms를 Burger ROS 2 통신의 보장 지연으로 써도 되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
안 된다. 원문은 7 sample에서 관찰된 최대 지연으로만 한정한다.
:::

## 실습 과제

원본 로그에서 sequence와 timestamp를 다시 짝지은 표를 만들고 관찰 범위와 과장 금지 문장을 함께 남긴다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 09 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 08 · 실제 Humble 증거 — turtlesim과 rqt_graph](08-실제-humble-증거-turtlesim과-rqt_graph.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 10 · ROS graph가 안 보이면 층을 나눈다](10-ros-graph가-안-보이면-층을-나눈다.md)
:::

::::
