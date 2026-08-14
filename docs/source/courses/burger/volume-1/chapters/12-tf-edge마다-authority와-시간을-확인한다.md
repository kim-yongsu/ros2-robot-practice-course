---
title: 12. TF edge마다 authority와 시간을 확인한다
source_pdf_page: 16
canonical_language: ko
course_id: burger-v1
volume: 1
part: 3
lesson: 12
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="12" data-lesson-title="TF edge마다 authority와 시간을 확인한다"></div>

<p class="lesson-kicker">PART 3 · 발견·좌표·TF·URDF / LESSON 12</p>

# 12. TF edge마다 authority와 시간을 확인한다

frame 이름만 보는 대신 각 변환을 누가 발행하며 어느 시각의 관계인지 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 16쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Burger TF tree의 map→odom→base_link→base_scan edge별 authority와 시간 특성을 정리한 도해.](/_static/generated/diagrams/burger/volume-1/figure-13.png)

## 학습 목표

- map→odom, odom→base_link, base_link→base_scan의 일반적 authority를 구분한다.
- Burger Humble URDF의 LiDAR frame인 `base_scan`을 확인한다.
- frame 부재와 Extrapolation 오류의 첫 검사 항목을 나눈다.

## 선수 조건

- Lesson 11의 frame·stamp 해석
- TF가 실행 중이거나 해당 항목을 HOLD로 둘 준비

## 핵심 개념

| TF edge | 일반적인 authority | 특성 |
| --- | --- | --- |
| `map → odom` | Localization 또는 SLAM | 전역 보정·점프 가능 |
| `odom → base_link` | Odometry source | 연속적이지만 drift 가능 |
| `base_link → base_scan` | URDF·robot_state_publisher | Burger의 고정 sensor 관계 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 run tf2_ros tf2_echo map base_link
ros2 run tf2_ros tf2_echo base_link base_scan
ros2 run tf2_ros tf2_monitor map base_link
ros2 run tf2_tools view_frames
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 각 edge가 존재하는지와 시간 흐름을 확인한다.
- `base_link → base_scan`이 Burger의 고정 sensor 관계로 나타나는지 본다.

## 관찰 포인트

- frame이 없으면 연결·이름을 먼저 본다.
- Extrapolation이면 stamp·시계 동기화·지연을 먼저 본다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
필요한 TF chain과 edge별 authority·시간을 실제 출력에서 확인한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
frame 이름만 알고 authority 또는 시간 증거가 없다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
TF 오류 종류를 구분하지 않고 static transform 추가로 덮어쓴다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- map→base_link 하나만 보고 중간 edge를 생략
- frame 부재와 시간 extrapolation을 같은 문제로 처리
- LiDAR frame을 설치본 확인 없이 다른 이름으로 고정

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `tf2_echo` 두 관계 출력
- [ ] `tf2_monitor` 시간 정보
- [ ] `view_frames` 생성물과 실행 시각

## 확인 문제

**질문:** Extrapolation 오류가 나면 가장 먼저 frame 이름만 바꿔야 하는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. frame 부재와 달리 Extrapolation은 stamp·시계 동기화·지연을 먼저 확인한다.
:::

## 실습 과제

현재 TF tree에서 세 edge의 authority와 시간 특성을 표로 채우고 없는 edge는 추정하지 말고 HOLD로 남긴다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 12 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 11 · PoseStamped는 frame·time·position·orientation 계약이다](11-posestamped는-frame-time-position-orientation-계약이다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 13 · URDF와 robot_state_publisher의 책임을 나눈다](13-urdf와-robot_state_publisher의-책임을-나눈다.md)
:::

::::
