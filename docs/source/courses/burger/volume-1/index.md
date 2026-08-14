---
title: Burger 1권 · ROS 2 Humble
canonical_language: ko
course_id: burger-v1
volume: 1
status: publication-candidate
sd_hide_title: true
---

# Burger 1권 · ROS 2 Humble

<div class="volume-hero">
  <div>
    <p class="hero-eyebrow">VOLUME 1 · TURTLEBOT3 BURGER · ROS 2 HUMBLE</p>
    <p class="course-hero-title" role="heading" aria-level="1">환경 기준선에서 재현 가능한 프로젝트까지</p>
    <p>6개 PART와 25개 Lesson을 따라가며 목표·명령·결과·STOP·증거·다음 학습을 한 화면에서 확인한다.</p>
    <div class="hero-actions">
      <a class="course-button course-button-primary" href="start.html">처음부터 시작</a>
      <a class="course-button course-button-secondary" href="start.html" data-course-resume-link>마지막 학습 이어보기</a>
    </div>
  </div>
  <div class="volume-cover" aria-label="Burger 1권 표지형 그래픽">
    <span>ROS 2</span><strong>BURGER</strong><small>VOLUME 1</small>
  </div>
</div>

<div class="course-progress-summary" data-course-progress-summary data-course-id="burger-v1">
  <div class="progress-copy"><strong>학습 진행률</strong><span data-progress-text>0 / 25 Lesson</span></div>
  <div class="progress-track" role="progressbar" aria-valuemin="0" aria-valuemax="25" aria-valuenow="0" aria-label="Burger 1권 완료 Lesson 수"><span data-progress-bar></span></div>
  <button type="button" class="progress-reset" data-course-progress-reset>진행률 초기화</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>

## 6 PART 학습 지도

::::{grid} 1 2 3 3
:gutter: 3
:class-container: part-card-grid

:::{grid-item-card} PART 1 · 환경 기준선
:class-item: part-card part-1
**Lesson 01–04**

OS · ROS · shell · workspace 기준선을 기록하고 같은 환경을 다시 복구한다.

[PART 시작](./part-01-environment/index.md)
:::
:::{grid-item-card} PART 2 · ROS 2 통신과 실행 증거
:class-item: part-card part-2
**Lesson 05–09**

Package부터 Node까지의 실행 관계와 Topic·Service·Action·Parameter의 계약을 증거로 설명한다.

[PART 시작](./part-02-communication/index.md)
:::
:::{grid-item-card} PART 3 · 발견·좌표·TF·URDF
:class-item: part-card part-3
**Lesson 10–13**

ROS graph, PoseStamped, TF edge, robot_state_publisher를 서로 다른 진단층으로 읽는다.

[PART 시작](./part-03-frames/index.md)
:::
:::{grid-item-card} PART 4 · 실물 명령과 시뮬레이션
:class-item: part-card part-4
**Lesson 14–17**

실물 주행 전 Gate와 STOP을 확인하고 simulation과 실물 증거를 혼동하지 않는다.

[PART 시작](./part-04-hardware-sim/index.md)
:::
:::{grid-item-card} PART 5 · SLAM·Localization·Nav2
:class-item: part-card part-5
**Lesson 18–21**

지도·현재 위치·Goal 상태·Cancel을 분리하고 source-supported 기준으로 판정한다.

[PART 시작](./part-05-navigation/index.md)
:::
:::{grid-item-card} PART 6 · 진단·증거·회귀·프로젝트
:class-item: part-card part-6
**Lesson 22–25**

실패·수정·rollback·증거·인수인계를 같은 실행 조건으로 재현한다.

[PART 시작](./part-06-evidence/index.md)
:::

::::

## 학습 전 요구사항

- [읽는 법](reading-guide.md)에서 VERIFY·STOP·HOLD 원칙을 먼저 확인한다.
- [6단계 학습 지도](learning-map.md)에서 각 PART의 입력·출력 관계를 확인한다.
- 실물 시험은 넓은 바닥·정지 담당·전원 차단 수단이 준비된 경우에만 진행한다.
- 실제 출력·물리 반응·지도·Nav2 Result가 없으면 해당 항목을 `HOLD`로 유지한다.

## 학습 도구

::::{grid} 1 1 3 3
:gutter: 2

:::{grid-item-card} 문제 해결
첫 실패 계층부터 자른다.

[진단 사다리](troubleshooting.md)
:::

:::{grid-item-card} 실습 과제
Source-supported 과제만 제공한다.

[연습 열기](exercises.md)
:::

:::{grid-item-card} PDF·Release
원문 snapshot과 배포 artifact를 확인한다.

[Release 열기](https://github.com/kim-yongsu/ros2-robot-practice-course/releases)
:::

::::

```{toctree}
:hidden:
:maxdepth: 2

start
reading-guide
learning-map
part-01-environment/index
part-02-communication/index
part-03-frames/index
part-04-hardware-sim/index
part-05-navigation/index
part-06-evidence/index
troubleshooting
exercises
```
