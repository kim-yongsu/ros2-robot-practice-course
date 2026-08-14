---
title: 21. NavigateToPose는 모듈형 ament_python 패키지로 만든다
source_pdf_page: 25
canonical_language: ko
course_id: burger-v1
volume: 1
part: 5
lesson: 21
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="21" data-lesson-title="NavigateToPose는 모듈형 ament_python 패키지로 만든다"></div>

<p class="lesson-kicker">PART 5 · SLAM·Localization·Nav2 / LESSON 21</p>

# 21. NavigateToPose는 모듈형 ament_python 패키지로 만든다

Goal response·Feedback·Result·Cancel Future를 분리해 Accepted를 terminal success로 오판하지 않는다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 25쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ament_python package 구조와 NavigateToPose Goal·Feedback·Result·Cancel·Future 오류 경계를 분리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-22.png)

## 학습 목표

- ament_python package 생성·build·실행 흐름을 확인한다.
- SERVER_TIMEOUT·REJECTED·ACCEPTED·terminal GoalStatus·Future error를 분리한다.
- 문서에서 테스트된 실제 예제 source를 literalinclude로 포함한다.

## 선수 조건

- Lesson 20의 Nav2 네 Gate
- 공개 예제 `examples/burger/volume1/navigate_to_pose_client.py`

## 핵심 개념

| 상태·오류 | 정확한 뜻 | 종료 판정 |
| --- | --- | --- |
| SERVER_TIMEOUT | Action server 미발견 | Goal 미전송 |
| REJECTED | 서버가 Goal을 미수락 | 실패 종료 |
| ACCEPTED | 작업 시작 허가 | 아직 성공 아님 |
| terminal GoalStatus | SUCCEEDED / ABORTED / CANCELED | 각 결과 분리 |
| Future error | Goal / Result / Cancel 경계 예외 | 명시적 Outcome |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 \
  burger_nav2_goal_client \
  --dependencies rclpy nav2_msgs action_msgs geometry_msgs \
  builtin_interfaces
colcon build --symlink-install --packages-select burger_nav2_goal_client
source install/setup.bash
ros2 interface show nav2_msgs/action/NavigateToPose
ros2 run burger_nav2_goal_client go_to_pose --ros-args \
  -p x:=1.0 -p y:=0.0 -p yaw:=0.0
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- Action server 발견과 Goal response를 분리한다.
- Feedback 중 Cancel 요청과 terminal Result를 각각 처리한다.
- 예외가 Goal·Result·Cancel 중 어느 Future에서 발생했는지 Outcome으로 남긴다.

## 관찰 포인트

- 동반 예제의 정적·순수 로직 시험과 Humble colcon·DDS·Nav2·실물 통합시험을 분리한다.
- Cancel을 물리 비상정지라고 부르지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
Accepted와 terminal Result를 구분하고 source·test·runtime 증거층을 명시한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
완전한 ROS package tree·maintainer identity·license·Humble colcon 증거가 아직 확인되지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
누락된 package 파일을 추정해 조립하거나 Accepted 로그를 success로 기록한다.
:::

::::

## STOP 조건

:::{danger}
Cancel은 software-level Action 상태다. 물리 위험에서는 별도 정지·전원 차단 수단을 사용한다.
:::

## 실패·문제해결

- Goal response와 Result Future를 하나로 처리
- Cancel 완료를 물리 정지로 오해
- 문서에 예제 코드를 복사해 테스트 source와 불일치

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] interface 정의와 실행 명령
- [ ] Goal·Feedback·Result·Cancel 상태 log
- [ ] 예제 source test와 runtime HOLD 범위

## 확인 문제

**질문:** Goal이 Accepted된 시점에 `SUCCEEDED`를 기록해도 되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
안 된다. Accepted는 시작 허가이며 terminal GoalStatus를 별도로 기다려야 한다.
:::

## 실습 과제

예제의 상태 전이를 SERVER_TIMEOUT / REJECTED / ACCEPTED / terminal / Future error 다섯 갈래로 그려 보고 각 종료 조건을 적는다.


## 공개 예제 source

:::{warning}
이 공개 교재에는 단일 파일 교육 예제만 포함한다. 완전한 ROS package source는 실제 package tree, maintainer identity, license, Humble `colcon build/test` 증거가 함께 확인될 때 `ros2_ws/src`에 추가한다. 누락된 파일을 추정해 조립하지 않는다.
:::

아래 코드는 `examples/`의 실제 파일을 직접 포함한다.

```{literalinclude} ../../../../../../examples/burger/volume1/navigate_to_pose_client.py
:language: python
:linenos:
```

## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 21 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 20 · Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다](20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 22 · 문제는 처음 깨진 계층에서 자른다](22-문제는-처음-깨진-계층에서-자른다.md)
:::

::::
