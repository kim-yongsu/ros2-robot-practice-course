---
title: 15. bringup은 일곱 게이트를 통과한 뒤 실행한다
source_pdf_page: 19
canonical_language: ko
course_id: burger-v1
volume: 1
part: 4
lesson: 15
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="15" data-lesson-title="bringup은 일곱 게이트를 통과한 뒤 실행한다"></div>

<p class="lesson-kicker">PART 4 · 실물 명령과 시뮬레이션 / LESSON 15</p>

# 15. bringup은 일곱 게이트를 통과한 뒤 실행한다

SSH 성공만으로 준비를 합격시키지 않고 안전·장치·네트워크·ROS 계약·bringup을 첫 FAIL에서 멈춘다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 19쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Remote PC와 SBC 책임을 분리해 안전·장치·네트워크·ROS 계약·bringup Gate를 검사하는 표.](/_static/generated/diagrams/burger/volume-1/figure-16.png)

## 학습 목표

- Remote PC와 SBC 책임을 분리한다.
- 안전·전원, 장치, 네트워크, ROS 계약, bringup Gate를 순서대로 확인한다.
- port와 LDS 모델을 실제 설치본에서 재확인한다.

## 선수 조건

- Lesson 14의 명령·device·물리 증거 경계
- 넓은 바닥·정지 담당·전원 차단 수단

## 핵심 개념

| Gate | PASS 기준 | FAIL이면 |
| --- | --- | --- |
| 안전·전원 | 넓은 바닥·정지 담당·배터리·케이블 | 전원 차단 후 재배치 |
| 장치 | OpenCR·LDS port와 권한 확인 | 케이블·udev·firmware |
| 네트워크 | IP·SSH·multicast 경로 | ROS 이전 연결 복구 |
| ROS 계약 | Humble·Domain·RMW·burger·LDS_MODEL | 환경변수·source 교정 |
| bringup | Node·Topic·TF·log가 함께 정상 | 첫 오류에서 원인 분리 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
# Remote PC → SBC
ssh ubuntu@<SBC_IP>

# TurtleBot3 SBC
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- SBC 접속 전에 안전·장치·네트워크 Gate를 확인한다.
- bringup 뒤 Node·Topic·TF·log를 함께 확인한다.

## 관찰 포인트

- `/dev/ttyACM0`과 `/dev/ttyUSB0`은 Humble launch 기본값일 수 있으나 실제 장비 영구값으로 단정하지 않는다.
- 첫 오류 위의 원인이 남아 있는지 본다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
모든 필요한 Gate가 실제 환경값과 log로 확인되고 첫 teleop 준비가 된다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
장치 port·권한·LDS 모델 또는 Node·Topic·TF·log 중 하나라도 확인되지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
SSH 성공만으로 bringup 준비를 PASS하거나 안전 Gate 없이 launch한다.
:::

::::

## STOP 조건

:::{danger}
주행 공간·정지 담당·배터리·케이블 Gate가 PASS하기 전에는 bringup 이후 구동 시험으로 진행하지 않는다.
:::

## 실패·문제해결

- SBC가 아닌 Remote PC에서 bringup 실행
- 기본 port를 장비 고정값으로 복사
- 여러 오류를 한꺼번에 고치며 첫 FAIL을 잃음

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 안전 담당·주행 공간·전원 상태
- [ ] 실제 device path·권한·LDS 설정
- [ ] 환경값·launch log·Node·Topic·TF

## 확인 문제

**질문:** SSH가 성공하면 bringup Gate는 끝난 것인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 장치, ROS 계약, Node·Topic·TF·log를 별도로 통과해야 한다.
:::

## 실습 과제

자신의 장비에서 각 Gate를 PASS/HOLD로 표기하고 첫 HOLD 하나만 다음 수정 대상으로 정한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 15 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 14 · /cmd_vel과 실제 바퀴 사이의 경계를 나눈다](14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 16 · 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다](16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다.md)
:::

::::
