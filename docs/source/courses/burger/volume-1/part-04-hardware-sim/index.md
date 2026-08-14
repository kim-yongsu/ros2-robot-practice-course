---
title: PART 4 · 실물 명령과 시뮬레이션
canonical_language: ko
course_id: burger-v1
part: 4
status: source-supported
---

<p class="part-kicker part-4">BURGER · VOLUME 1 · PART 4</p>

# PART 4 · 실물 명령과 시뮬레이션

명령에서 실제 wheel까지의 경계를 나누고 bringup·저속 teleop·Gazebo의 증명 범위를 닫는다.

<div class="part-summary part-4">
  <div><strong>선수 PART</strong><span>PART 3 발견·좌표·TF·URDF</span></div>
  <div><strong>완료 능력</strong><span>실물 주행 전 Gate와 STOP을 확인하고 simulation과 실물 증거를 혼동하지 않는다.</span></div>
  <div><strong>Lesson</strong><span>4개 · 14–17</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 14
:class-item: lesson-card
**/cmd_vel과 실제 바퀴 사이의 경계를 나눈다**

명령 발행, SBC 수신, OpenCR 전달, 실제 wheel 반응을 서로 다른 증거층으로 확인한다.

[학습하기](../chapters/14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다.md)
:::

:::{grid-item-card} Lesson 15
:class-item: lesson-card
**bringup은 일곱 게이트를 통과한 뒤 실행한다**

SSH 성공만으로 준비를 합격시키지 않고 안전·장치·네트워크·ROS 계약·bringup을 첫 FAIL에서 멈춘다.

[학습하기](../chapters/15-bringup은-일곱-게이트를-통과한-뒤-실행한다.md)
:::

:::{grid-item-card} Lesson 16
:class-item: lesson-card
**첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다**

최대 속도 대신 입력·정지·publisher 종료·물리 정지를 짧은 폐루프로 확인한다.

[학습하기](../chapters/16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다.md)
:::

:::{grid-item-card} Lesson 17
:class-item: lesson-card
**Gazebo Classic은 Humble 가상 증거로만 사용한다**

fake node·Gazebo Classic·실물 Burger가 각각 증명하고 증명하지 못하는 범위를 나눈다.

[학습하기](../chapters/17-gazebo-classic은-humble-가상-증거로만-사용한다.md)
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
[← PART 3 · 발견·좌표·TF·URDF](../part-03-frames/index.md)
:::

:::{grid-item-card} 다음
[PART 5 · SLAM·Localization·Nav2 →](../part-05-navigation/index.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다
../chapters/15-bringup은-일곱-게이트를-통과한-뒤-실행한다
../chapters/16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다
../chapters/17-gazebo-classic은-humble-가상-증거로만-사용한다
```
