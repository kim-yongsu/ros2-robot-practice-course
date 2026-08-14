---
title: 19. Initial Pose는 scan-map 정합으로 판정한다
source_pdf_page: 23
canonical_language: ko
course_id: burger-v1
volume: 1
part: 5
lesson: 19
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="19" data-lesson-title="Initial Pose는 scan-map 정합으로 판정한다"></div>

<p class="lesson-kicker">PART 5 · SLAM·Localization·Nav2 / LESSON 19</p>

# 19. Initial Pose는 scan-map 정합으로 판정한다

RViz 아이콘만 보지 않고 AMCL scan 점이 저장 지도 벽과 위치·yaw 모두 맞는지 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 23쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Initial Pose와 map origin을 구분하고 scan-map 위치·yaw 정합을 판정하는 도해.](/_static/generated/diagrams/burger/volume-1/figure-20.png)

## 학습 목표

- Initial Pose와 map origin을 구분한다.
- 아이콘 위치와 scan-map 정합을 별도 증거로 본다.
- x·y 평행 오차와 yaw 회전 오차를 구분해 수정한다.

## 선수 조건

- Lesson 18의 지도 파일·품질 Gate
- Navigation2 launch와 저장 지도 경로

## 핵심 개념

| 관찰 | 정확한 뜻 | 다음 행동 |
| --- | --- | --- |
| Initial Pose | AMCL particle의 시작 위치·yaw | 실제 위치에 맞게 지정 |
| 아이콘 위치 | RViz 표시 | scan과 벽을 함께 확인 |
| scan 평행 이동 | x·y 오차 가능 | 위치를 다시 지정 |
| scan 회전 오차 | yaw 오차 가능 | 방향을 다시 지정 |
| 짧은 teleop | belief 수렴 보조 | `Ctrl+C` 후 Goal 준비 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:="$HOME/maps/classroom_v1.yaml"
# RViz: 2D Pose Estimate → scan-map 정합
ros2 run tf2_ros tf2_echo map base_link
ros2 topic info /cmd_vel --verbose
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 실제 위치·yaw에 Initial Pose를 지정한다.
- scan 점과 지도 벽의 위치·방향 정합을 확인한다.
- Goal 전 teleop publisher가 종료됐는지 확인한다.

## 관찰 포인트

- Initial Pose는 map origin 선언이 아니다.
- 로봇 아이콘 위치만으로 localization proof가 되지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
scan-map 정합과 map→base_link, command ownership을 함께 확인한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
아이콘만 확인했고 scan-map 정합 또는 TF를 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
teleop publisher를 남긴 채 Goal을 보내거나 Initial Pose를 map origin으로 설명한다.
:::

::::

## STOP 조건

:::{danger}
짧은 teleop으로 수렴을 보조했다면 Goal 전 `Ctrl+C`로 publisher를 종료하고 물리 정지를 확인한다.
:::

## 실패·문제해결

- 아이콘이 지도 안에 있다는 이유로 localization PASS
- x·y와 yaw 오차를 구분하지 않음
- teleop 종료 확인 없이 Nav2로 전환

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] Initial Pose 전후 RViz 캡처
- [ ] scan-map 정합 관찰
- [ ] map→base_link TF와 `/cmd_vel` publisher 상태

## 확인 문제

**질문:** RViz 로봇 아이콘이 맞는 위치에 있으면 localization이 증명되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. scan 점과 지도 벽의 위치·yaw 정합을 함께 확인해야 한다.
:::

## 실습 과제

Initial Pose를 지정한 뒤 x·y 오차, yaw 오차, 정상 정합의 관찰 기준을 세 줄로 기록한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 19 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 18 · SLAM은 지도 품질과 파일 계약까지 닫는다](18-slam은-지도-품질과-파일-계약까지-닫는다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 20 · Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다](20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다.md)
:::

::::
