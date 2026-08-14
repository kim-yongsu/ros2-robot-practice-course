---
title: PART 1 · 환경 기준선
canonical_language: ko
course_id: burger-v1
part: 1
status: source-supported
---

<p class="part-kicker part-1">BURGER · VOLUME 1 · PART 1</p>

# PART 1 · 환경 기준선

Burger 학습을 시작하기 전에 터미널, OS, ROS 배포판, source와 workspace 계보를 고정한다.

<div class="part-summary part-1">
  <div><strong>선수 PART</strong><span>없음 · 1권의 시작점</span></div>
  <div><strong>완료 능력</strong><span>OS · ROS · shell · workspace 기준선을 기록하고 같은 환경을 다시 복구한다.</span></div>
  <div><strong>Lesson</strong><span>4개 · 01–04</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 01
:class-item: lesson-card
**Burger로 ROS 2의 공통 기준선을 만든다**

TurtleBot3 Burger를 환경·통신·좌표·실물·자율주행·유지보수 계약을 한 번에 확인하는 기준 플랫폼으로 사용한다.

[학습하기](../chapters/01-burger로-ros-2의-공통-기준선을-만든다.md)
:::

:::{grid-item-card} Lesson 02
:class-item: lesson-card
**터미널·Linux 생존선을 먼저 확보한다**

ROS 명령 전에 경로·권한·shell·실행 위치와 process 종료 능력을 고정한다.

[학습하기](../chapters/02-터미널-linux-생존선을-먼저-확보한다.md)
:::

:::{grid-item-card} Lesson 03
:class-item: lesson-card
**Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다**

OS·ROS 배포판·source 순서·Domain·RMW를 기록해 같은 명령이 다른 graph를 만드는 원인을 줄인다.

[학습하기](../chapters/03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다.md)
:::

:::{grid-item-card} Lesson 04
:class-item: lesson-card
**ISO·APT·GitHub·workspace의 계보를 분리한다**

운영체제 이미지, APT underlay, GitHub source, 로컬 workspace를 서로 다른 설치·삭제·rollback 층으로 관리한다.

[학습하기](../chapters/04-iso-apt-github-workspace의-계보를-분리한다.md)
:::

::::

## PART 점검

- [ ] 각 Lesson의 목표와 선수 조건을 확인했다.
- [ ] 실제 출력과 물리 결과가 없는 항목은 `HOLD`로 남겼다.
- [ ] 다음 PART 입력으로 사용할 명령·로그·관찰·hash 위치를 기록했다.
- [ ] STOP 조건과 복구 시작점을 설명할 수 있다.

## 이전 / 다음 PART

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} 이전
[← 1권 시작](../start.md)
:::

:::{grid-item-card} 다음
[PART 2 · ROS 2 통신과 실행 증거 →](../part-02-communication/index.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/01-burger로-ros-2의-공통-기준선을-만든다
../chapters/02-터미널-linux-생존선을-먼저-확보한다
../chapters/03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다
../chapters/04-iso-apt-github-workspace의-계보를-분리한다
```
