---
title: 16. 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다
source_pdf_page: 20
canonical_language: ko
course_id: burger-v1
volume: 1
part: 4
lesson: 16
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="16" data-lesson-title="첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다"></div>

<p class="lesson-kicker">PART 4 · 실물 명령과 시뮬레이션 / LESSON 16</p>

# 16. 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다

최대 속도 대신 입력·정지·publisher 종료·물리 정지를 짧은 폐루프로 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 20쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Burger 첫 teleop을 준비·0.01 m/s 전진·정지·회전·Ctrl+C로 닫는 안전 폐루프 도해.](/_static/generated/diagrams/burger/volume-1/figure-17.png)

## 학습 목표

- 첫 주행을 한 단계 전진과 즉시 정지로 제한한다.
- software stop과 물리 E-stop을 구분한다.
- 입력·command·publisher 제거·wheel 정지를 같은 회차에서 확인한다.

## 선수 조건

- Lesson 15 bringup Gate PASS
- 넓은 바닥·정지 담당·전원 차단 준비

## 핵심 개념

| 단계 | 행동 | 증거 |
| --- | --- | --- |
| 준비 | bringup 유지·바닥 확보·정지 담당 | 주행 반경과 전원 차단 |
| 전진 | `w` 한 번 → 짧게 관찰 | target +0.01 m/s |
| 정지 | `space` 또는 `s` | 0 command + 실제 wheel 정지 |
| 회전 | `a`·`d` 한 단계씩 후 즉시 stop | 좌·우 방향·부호 |
| 종료 | `Ctrl+C` | publisher 제거·wheel 정지 재확인 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
# Remote PC
export TURTLEBOT3_MODEL=burger
ros2 run turtlebot3_teleop teleop_keyboard

# 다른 terminal
ros2 topic info /cmd_vel --verbose
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- `w` 한 번의 target 증가와 즉시 stop을 확인한다.
- 좌·우 회전 부호를 한 단계씩 확인한다.
- `Ctrl+C` 뒤 publisher 제거와 wheel 정지를 재확인한다.

## 관찰 포인트

- Burger 최대 0.22 m/s는 source 제한값이며 첫 시험 목표가 아니다.
- software stop을 물리 비상정지라고 부르지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
저속 한 단계·즉시 정지·publisher 종료·물리 정지를 한 회차에서 증명한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
command 0만 확인했고 실제 wheel 정지 또는 publisher 제거를 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
table 위·무감시·최대 속도 시험 또는 정지 수단 없이 주행한다.
:::

::::

## STOP 조건

:::{danger}
table 위 시험과 무감시 시험은 NO-GO다. 예상 밖 움직임이 있으면 물리 정지와 전원 차단을 먼저 수행한다.
:::

## 실패·문제해결

- `w`를 반복 입력해 속도를 올림
- 0 command만 보고 wheel 정지 PASS
- Ctrl+C 후 남은 publisher 확인 생략

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 주행 전 안전 사진 또는 점검표
- [ ] `/cmd_vel` publisher·값
- [ ] wheel 이동·정지와 Ctrl+C 후 상태

## 확인 문제

**질문:** 0.22 m/s가 Burger의 제한값이면 첫 teleop도 그 속도로 해야 하는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 원문은 첫 시험을 0.01 m/s 한 단계와 즉시 정지로 제한한다.
:::

## 실습 과제

한 단계 전진·정지·좌회전·정지·우회전·정지·Ctrl+C 순서를 실행하고 각 단계 증거를 한 줄씩 남긴다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 16 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 15 · bringup은 일곱 게이트를 통과한 뒤 실행한다](15-bringup은-일곱-게이트를-통과한-뒤-실행한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 17 · Gazebo Classic은 Humble 가상 증거로만 사용한다](17-gazebo-classic은-humble-가상-증거로만-사용한다.md)
:::

::::
