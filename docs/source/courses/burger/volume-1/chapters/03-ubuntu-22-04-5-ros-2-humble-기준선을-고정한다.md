---
title: 3. Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다
source_pdf_page: 7
canonical_language: ko
course_id: burger-v1
volume: 1
part: 1
lesson: 3
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="03" data-lesson-title="Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다"></div>

<p class="lesson-kicker">PART 1 · 환경 기준선 / LESSON 03</p>

# 3. Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다

OS·ROS 배포판·source 순서·Domain·RMW를 기록해 같은 명령이 다른 graph를 만드는 원인을 줄인다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 7쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Ubuntu·ROS_DISTRO·TURTLEBOT3_MODEL·Domain·RMW 기준값과 불일치 조치를 정리한 표.](/_static/generated/diagrams/burger/volume-1/figure-04.png)

## 학습 목표

- Humble 실행 환경의 기준값을 명령으로 수집한다.
- OS·ROS_DISTRO·TURTLEBOT3_MODEL·Domain·RMW 불일치를 구분한다.
- 한 번에 한 변수만 바꾸는 변경 통제를 적용한다.

## 선수 조건

- Lesson 02의 장비·shell·경로 확인

## 핵심 개념

| 항목 | 잠금값 | 불일치 시 |
| --- | --- | --- |
| OS | Ubuntu 22.04.5 Jammy | 다음 단계 중지 |
| ROS_DISTRO | humble | source 계보 확인 |
| TURTLEBOT3_MODEL | burger | 실물·URDF·parameter 불일치 확인 |
| Domain·RMW | 시험 회차별 기록 | 양쪽 PC 기준선 대조 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
lsb_release -ds
printenv ROS_DISTRO
printenv ROS_DOMAIN_ID
printenv RMW_IMPLEMENTATION
printenv TURTLEBOT3_MODEL
which ros2
ros2 doctor --report
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- OS와 ROS 배포판이 1권 기준과 일치하는지 판별한다.
- Domain·RMW는 시험 회차별 실제 값을 남긴다.
- `which ros2`와 `ros2 doctor --report`로 실행 계보를 보강한다.

## 관찰 포인트

- 양쪽 PC의 Domain·RMW·source 결과를 같은 표에서 비교한다.
- branch·RMW·Domain·parameter를 동시에 바꾸지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
기준 환경을 재현 가능한 텍스트로 기록하고 불일치 항목을 다음 단계 전에 해소한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
OS·ROS_DISTRO 또는 양쪽 장비의 Domain·RMW 기준이 확인되지 않는다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
여러 변수를 동시에 바꾼 뒤 어떤 변경이 결과를 만들었는지 설명하지 못한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- 현재 shell이 아닌 과거 터미널의 환경값을 증거로 사용
- 빈 환경변수를 기본값과 같다고 추정
- 환경 불일치 상태에서 graph 문제로 바로 이동

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 환경 명령 전체 출력
- [ ] `ros2 doctor --report` 파일
- [ ] 변경 전후 한 변수 diff

## 확인 문제

**질문:** Domain·RMW·parameter를 한 번에 바꾸면 안 되는 이유는?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
결과 변화의 원인과 rollback 지점을 분리할 수 없기 때문이다.
:::

## 실습 과제

Remote PC와 SBC의 기준선을 같은 형식으로 수집해 서로 다른 값 하나를 표시하고, 수정할 변수는 하나만 선택한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 03 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 02 · 터미널·Linux 생존선을 먼저 확보한다](02-터미널-linux-생존선을-먼저-확보한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 04 · ISO·APT·GitHub·workspace의 계보를 분리한다](04-iso-apt-github-workspace의-계보를-분리한다.md)
:::

::::
