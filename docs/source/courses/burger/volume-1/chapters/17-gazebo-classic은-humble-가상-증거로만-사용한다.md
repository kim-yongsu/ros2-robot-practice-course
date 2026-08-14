---
title: 17. Gazebo Classic은 Humble 가상 증거로만 사용한다
source_pdf_page: 21
canonical_language: ko
course_id: burger-v1
volume: 1
part: 4
lesson: 17
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="17" data-lesson-title="Gazebo Classic은 Humble 가상 증거로만 사용한다"></div>

<p class="lesson-kicker">PART 4 · 실물 명령과 시뮬레이션 / LESSON 17</p>

# 17. Gazebo Classic은 Humble 가상 증거로만 사용한다

fake node·Gazebo Classic·실물 Burger가 각각 증명하고 증명하지 못하는 범위를 나눈다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 21쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Fake node·Gazebo Classic·실물 Burger가 증명하는 것과 증명하지 못하는 것을 비교한 도해.](/_static/generated/diagrams/burger/volume-1/figure-18.png)

## 학습 목표

- Humble의 Gazebo Classic 경로와 Jazzy의 Gazebo Sim 경로를 섞지 않는다.
- simulation이 모델·가상 sensor·collision을 확인하는 범위를 설명한다.
- OpenCR·battery·실제 wheel은 실물 증거로 남긴다.

## 선수 조건

- Lesson 14~16의 실물 명령·정지 경계
- Humble branch workspace 또는 미설치 HOLD

## 핵심 개념

| 환경 | 증명 가능한 것 | 증명하지 못하는 것 |
| --- | --- | --- |
| Fake node | 모델·joint·TF·RViz 표현 | sensor·physics·collision |
| Gazebo Classic | spawn·sim time·가상 scan/odom·collision | OpenCR·USB·battery·실제 wheel |
| 실물 Burger | device·firmware·motor·정지 거리 | simulation determinism |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
cd ~/turtlebot3_ws/src
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
source install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- Humble branch를 build·source하고 Gazebo Classic world를 launch한다.
- spawn·sim time·가상 scan/odom·collision을 simulation evidence로만 기록한다.

## 관찰 포인트

- OpenCR·USB·battery·실제 wheel은 simulation 결과에 포함시키지 않는다.
- Jazzy ros_gz 명령을 이 Humble Lesson에 병합하지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
가상 모델·sensor·collision 증거와 실물 HOLD 범위를 명시한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
Gazebo runtime을 실행하지 않았거나 가상 scan/odom·collision을 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
Gazebo 성공을 OpenCR·battery·실제 wheel의 PASS로 기록한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- Humble과 Jazzy 명령 혼합
- world spawn만 보고 sensor·collision까지 PASS
- simulation 결과로 실물 정지 거리 주장

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] branch·commit·build 결과
- [ ] launch log와 sim time
- [ ] 가상 scan/odom·collision 관찰 및 실물 HOLD 표

## 확인 문제

**질문:** Gazebo Classic에서 wheel이 움직이면 실제 Burger motor와 battery도 정상인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. simulation은 OpenCR·USB·battery·실제 wheel을 증명하지 않는다.
:::

## 실습 과제

Fake node·Gazebo Classic·실물 세 환경의 증명 범위를 자신의 evidence 항목으로 다시 분류한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 17 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 16 · 첫 teleop은 0.01 m/s 한 단계와 즉시 정지로 시작한다](16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 18 · SLAM은 지도 품질과 파일 계약까지 닫는다](18-slam은-지도-품질과-파일-계약까지-닫는다.md)
:::

::::
