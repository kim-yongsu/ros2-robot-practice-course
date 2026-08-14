---
title: 2. 터미널·Linux 생존선을 먼저 확보한다
source_pdf_page: 6
canonical_language: ko
course_id: burger-v1
volume: 1
part: 1
lesson: 2
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="02" data-lesson-title="터미널·Linux 생존선을 먼저 확보한다"></div>

<p class="lesson-kicker">PART 1 · 환경 기준선 / LESSON 02</p>

# 2. 터미널·Linux 생존선을 먼저 확보한다

ROS 명령 전에 경로·권한·shell·실행 위치와 process 종료 능력을 고정한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 6쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Remote PC와 Burger SBC에서 위치·파일·ROS 환경·process 종료를 확인하는 Linux 생존선 표.](/_static/generated/diagrams/burger/volume-1/figure-03.png)

## 학습 목표

- 현재 터미널의 위치와 파일·권한을 확인한다.
- Remote PC와 Burger SBC의 실행 책임을 구분한다.
- 현재 shell에 ROS 2 Humble 환경이 적용됐는지 확인하고 process를 종료한다.

## 선수 조건

- Lesson 01의 판정 원칙
- Remote PC와 Burger SBC를 구분할 수 있는 표식 또는 hostname

## 핵심 개념

| 질문 | 정상 기준 | 첫 명령 |
| --- | --- | --- |
| 지금 어디에 있는가? | 예상한 작업 경로 | `pwd` |
| 어떤 파일이 있는가? | 오타 없는 파일·권한 | `ls -la` |
| ROS 환경이 적용됐는가? | `ROS_DISTRO=humble` | `printenv ROS_DISTRO` |
| process를 멈출 수 있는가? | `Ctrl+C`로 종료 | `ps -ef` / `Ctrl+C` |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
pwd
ls -la
hostname
printenv ROS_DISTRO
ps -ef
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- `pwd`와 `hostname`이 의도한 장비·경로를 가리킨다.
- `printenv ROS_DISTRO`가 현재 shell의 배포판을 보여 준다.
- 실행한 process를 `Ctrl+C`로 종료할 수 있다.

## 관찰 포인트

- 프롬프트의 `$`, 사용자명, hostname을 명령으로 붙여넣지 않았는지 본다.
- 같은 명령을 다른 PC에서 실행하지 않았는지 `hostname`과 `pwd`로 확인한다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
장비·경로·ROS_DISTRO를 확인하고 실행 process를 의도대로 종료한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
Remote PC와 SBC 역할이 불명확하거나 현재 shell의 ROS 환경이 확인되지 않는다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
실물 로봇이 예상과 다르게 움직이는데 키보드 입력만 반복하거나 물리 정지 수단이 없다.
:::

::::

## STOP 조건

:::{danger}
실물 로봇이 예상과 다르게 움직이면 키보드보다 물리 정지와 전원 차단 수단을 먼저 사용한다.
:::

## 실패·문제해결

- 터미널 프롬프트 전체를 명령으로 복사
- source하지 않은 새 shell에서 ROS 명령 실행
- Remote PC 명령을 SBC에서 또는 반대로 실행

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `hostname`·`pwd` 결과
- [ ] `printenv ROS_DISTRO` 결과
- [ ] process 시작·Ctrl+C 종료 기록

## 확인 문제

**질문:** 새 터미널에서 `ros2` 명령이 되지 않을 때 가장 먼저 확인할 것은?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
현재 shell에 필요한 `setup.bash`가 적용됐는지와 `ROS_DISTRO`를 먼저 확인한다.
:::

## 실습 과제

Remote PC와 SBC에서 각각 `hostname`, `pwd`, `printenv ROS_DISTRO`를 실행하고 두 장비의 책임을 한 표에 기록한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 02 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 01 · Burger로 ROS 2의 공통 기준선을 만든다](01-burger로-ros-2의-공통-기준선을-만든다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 03 · Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다](03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다.md)
:::

::::
