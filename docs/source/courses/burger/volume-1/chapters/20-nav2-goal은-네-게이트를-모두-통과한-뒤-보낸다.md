---
title: 20. Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다
source_pdf_page: 24
canonical_language: ko
course_id: burger-v1
volume: 1
part: 5
lesson: 20
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="20" data-lesson-title="Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다"></div>

<p class="lesson-kicker">PART 5 · SLAM·Localization·Nav2 / LESSON 20</p>

# 20. Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다

Lifecycle·TF/Pose·global/local costmap·Action/command ownership을 독립 Gate로 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 24쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Nav2 Goal 전 Lifecycle·TF/Pose·global/local costmap·Action/command/STOP 네 Gate를 검사하는 도해.](/_static/generated/diagrams/burger/volume-1/figure-21.png)

## 학습 목표

- Nav2 managed node의 lifecycle 상태를 확인한다.
- TF·현재 pose와 global/local costmap 입력을 분리한다.
- Action server·command publisher·STOP 준비를 Goal 전 확인한다.

## 선수 조건

- Lesson 18 지도 품질·파일 계약
- Lesson 19 scan-map 정합

## 핵심 개념

| Gate | PASS 기준 | FAIL 시 우선 확인 |
| --- | --- | --- |
| Lifecycle | 관련 server active | configure·activate·bond |
| TF·Pose | map→odom→base와 current pose 안정 | Localization·시간 |
| Costmaps | global map·footprint·layer / local sensor·obstacle update | Planner·Controller·sensor source |
| Action·command·STOP | server·publisher ownership·정지 수단 준비 | 중복 publisher·topic type |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 lifecycle nodes
ros2 lifecycle get /planner_server
ros2 lifecycle get /controller_server
ros2 action info /navigate_to_pose
ros2 param dump /global_costmap/global_costmap
ros2 param dump /local_costmap/local_costmap
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 관련 lifecycle server가 active인지 확인한다.
- TF·current pose와 두 costmap의 source를 점검한다.
- Action server와 `/cmd_vel` ownership·STOP을 확인한다.

## 관찰 포인트

- Node 이름·plugin·cmd_vel type은 설치본에서 탐지한다.
- Path 생성과 command·base motion·Goal 성공을 다른 증거로 둔다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
네 Gate가 각각 실제 상태·parameter·endpoint로 확인된 뒤 Goal을 보낼 준비가 된다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
Gate 하나라도 미확인·inactive·source 불명확 상태다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
Path가 생겼다는 이유로 command·base motion·terminal Goal 성공을 선언한다.
:::

::::

## STOP 조건

:::{danger}
command ownership과 정지 수단이 준비되지 않았으면 Goal을 보내지 않는다.
:::

## 실패·문제해결

- lifecycle 상태를 보지 않고 Goal 전송
- global과 local costmap source 혼동
- 중복 command publisher를 남김

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] lifecycle node·server 상태
- [ ] TF·current pose
- [ ] global/local costmap parameter
- [ ] Action·publisher·STOP 점검표

## 확인 문제

**질문:** RViz에 Path가 생성되면 NavigateToPose 성공인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. command 발행, base motion, terminal Goal Result를 각각 확인해야 한다.
:::

## 실습 과제

네 Gate를 한 표에 채우고 하나라도 HOLD면 Goal 전송 대신 첫 HOLD의 복구 절차를 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 20 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 19 · Initial Pose는 scan-map 정합으로 판정한다](19-initial-pose는-scan-map-정합으로-판정한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 21 · NavigateToPose는 모듈형 ament_python 패키지로 만든다](21-navigatetopose는-모듈형-ament_python-패키지로-만든다.md)
:::

::::
