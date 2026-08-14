---
title: ROS 2 로봇 실습 강좌
canonical_language: ko
course_id: ros2-robot-practice-course
status: publication-candidate
sd_hide_title: true
---

# ROS 2 로봇 실습 강좌

<div class="course-hero">
  <div class="course-hero-copy">
    <p class="hero-eyebrow">ROS 2 HUMBLE · TURTLEBOT3 BURGER</p>
    <p class="course-hero-title" role="heading" aria-level="1">실행하고, 판정하고, 증거를 남기는 ROS 2 로봇 실습 강좌</p>
    <p>파일 트리를 헤매지 않고 6개 PART와 25개 Lesson을 순서대로 학습한다. 실제 값·STOP·복구·증거가 확인되지 않은 항목은 PASS로 만들지 않는다.</p>
    <div class="hero-actions">
      <a class="course-button course-button-primary" href="courses/burger/volume-1/start.html">Burger 1권 시작하기</a>
      <a class="course-button course-button-secondary" href="courses/burger/volume-1/start.html" data-course-resume-link>마지막 학습 이어보기</a>
    </div>
    <p class="privacy-note">진행률은 현재 브라우저에만 저장되며 서버로 전송되지 않는다.</p>
  </div>
  <div class="course-hero-art" aria-hidden="true">
    <span class="orbit orbit-a"></span><span class="orbit orbit-b"></span>
    <span class="robot-core">B1</span>
    <span class="hero-chip chip-a">TF</span><span class="hero-chip chip-b">Nav2</span><span class="hero-chip chip-c">Evidence</span>
  </div>
</div>

## 지금 공개된 강좌

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} TurtleBot3 Burger · 1권
:class-item: course-card course-card-active
**ROS 2 Humble 기준선부터 조별 프로젝트 완료 계약까지**

- 6 PART
- 25 Lesson
- 실물·simulation 경계
- PASS / HOLD / FAIL
- 로컬 진행률·이어보기

[1권 강좌 홈](courses/burger/volume-1/index.md)
:::

:::{grid-item-card} 후속 기체
:class-item: course-card course-card-disabled
**준비 중**

Waffle Pi · Waffle Pi Tank · C2 6축 MoMa는 완료 source가 들어오기 전까지 비활성 상태로 유지한다.

[준비 중 범위 확인](courses/index.md)
:::

::::

## 6단계 학습 로드맵

::::{grid} 1 2 3 3
:gutter: 2
:class-container: roadmap-grid

:::{grid-item-card} PART 1 · 환경 기준선
:class-item: roadmap-card part-1
Lesson 01–04 · 4개

Burger 학습을 시작하기 전에 터미널, OS, ROS 배포판, source와 workspace 계보를 고정한다.

[PART 열기](courses/burger/volume-1/part-01-environment/index.md)
:::
:::{grid-item-card} PART 2 · ROS 2 통신과 실행 증거
:class-item: roadmap-card part-2
Lesson 05–09 · 5개

실행 단위와 interface를 구분하고 이름이 아니라 type·endpoint·QoS·실제 message로 통신을 판정한다.

[PART 열기](courses/burger/volume-1/part-02-communication/index.md)
:::
:::{grid-item-card} PART 3 · 발견·좌표·TF·URDF
:class-item: roadmap-card part-3
Lesson 10–13 · 4개

발견 문제를 계층으로 자르고 좌표·시간·TF authority·URDF 책임을 분리한다.

[PART 열기](courses/burger/volume-1/part-03-frames/index.md)
:::
:::{grid-item-card} PART 4 · 실물 명령과 시뮬레이션
:class-item: roadmap-card part-4
Lesson 14–17 · 4개

명령에서 실제 wheel까지의 경계를 나누고 bringup·저속 teleop·Gazebo의 증명 범위를 닫는다.

[PART 열기](courses/burger/volume-1/part-04-hardware-sim/index.md)
:::
:::{grid-item-card} PART 5 · SLAM·Localization·Nav2
:class-item: roadmap-card part-5
Lesson 18–21 · 4개

지도 품질, Initial Pose, Nav2 전제조건, NavigateToPose Action 상태를 독립 Gate로 검증한다.

[PART 열기](courses/burger/volume-1/part-05-navigation/index.md)
:::
:::{grid-item-card} PART 6 · 진단·증거·회귀·프로젝트
:class-item: roadmap-card part-6
Lesson 22–25 · 4개

첫 실패 계층, RUN_ID, 회귀시험, 프로젝트 완료 계약을 한 폐루프로 묶는다.

[PART 열기](courses/burger/volume-1/part-06-evidence/index.md)
:::

::::

## 이 강좌를 사용하는 법

::::{grid} 1 1 3 3
:gutter: 2

:::{grid-item-card} 1 · 실행
명령 위치와 환경을 확인하고 source-supported 순서로 실행한다.
:::

:::{grid-item-card} 2 · 판정
정상 결과, STOP 조건, 첫 FAIL, 마지막 PASS를 분리한다.
:::

:::{grid-item-card} 3 · 증거
명령·로그·message·물리 관찰·hash를 같은 RUN_ID에 연결한다.
:::

::::

## 대상 독자

학생·교사·ROS 2 로봇 개발 신입·빠르게 interface와 evidence 위치를 재확인하려는 실무자를 대상으로 한다.

## 바로가기

- [PDF·Release](https://github.com/kim-yongsu/ros2-robot-practice-course/releases)
- [문제 해결](courses/burger/volume-1/troubleshooting.md)
- [실습 과제](courses/burger/volume-1/exercises.md)
- [GitHub 저장소](https://github.com/kim-yongsu/ros2-robot-practice-course)

```{toctree}
:hidden:
:maxdepth: 5

courses/index
limitations
supported-versions
```
