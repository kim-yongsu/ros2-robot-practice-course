---
title: PART 3 · 발견·좌표·TF·URDF
canonical_language: ko
course_id: burger-v1
part: 3
status: source-supported
---

<p class="part-kicker part-3">BURGER · VOLUME 1 · PART 3</p>

# PART 3 · 발견·좌표·TF·URDF

발견 문제를 계층으로 자르고 좌표·시간·TF authority·URDF 책임을 분리한다.

<div class="part-summary part-3">
  <div><strong>선수 PART</strong><span>PART 2 통신과 실행 증거</span></div>
  <div><strong>완료 능력</strong><span>ROS graph, PoseStamped, TF edge, robot_state_publisher를 서로 다른 진단층으로 읽는다.</span></div>
  <div><strong>Lesson</strong><span>4개 · 10–13</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 10
:class-item: lesson-card
**ROS graph가 안 보이면 층을 나눈다**

ping 하나로 ROS 통신을 판정하지 않고 환경 → 네트워크 → 발견 → interface 순서로 첫 실패 계층을 찾는다.

[학습하기](../chapters/10-ros-graph가-안-보이면-층을-나눈다.md)
:::

:::{grid-item-card} Lesson 11
:class-item: lesson-card
**PoseStamped는 frame·time·position·orientation 계약이다**

숫자만 읽지 않고 어느 frame에서 언제 측정한 위치와 회전인지 함께 해석한다.

[학습하기](../chapters/11-posestamped는-frame-time-position-orientation-계약이다.md)
:::

:::{grid-item-card} Lesson 12
:class-item: lesson-card
**TF edge마다 authority와 시간을 확인한다**

frame 이름만 보는 대신 각 변환을 누가 발행하며 어느 시각의 관계인지 확인한다.

[학습하기](../chapters/12-tf-edge마다-authority와-시간을-확인한다.md)
:::

:::{grid-item-card} Lesson 13
:class-item: lesson-card
**URDF와 robot_state_publisher의 책임을 나눈다**

모델 정의, joint 상태 입력, TF 발행, RViz 시각화를 하나의 프로그램 책임으로 섞지 않는다.

[학습하기](../chapters/13-urdf와-robot_state_publisher의-책임을-나눈다.md)
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
[← PART 2 · ROS 2 통신과 실행 증거](../part-02-communication/index.md)
:::

:::{grid-item-card} 다음
[PART 4 · 실물 명령과 시뮬레이션 →](../part-04-hardware-sim/index.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/10-ros-graph가-안-보이면-층을-나눈다
../chapters/11-posestamped는-frame-time-position-orientation-계약이다
../chapters/12-tf-edge마다-authority와-시간을-확인한다
../chapters/13-urdf와-robot_state_publisher의-책임을-나눈다
```
