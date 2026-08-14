---
title: PART 5 · SLAM·Localization·Nav2
canonical_language: ko
course_id: burger-v1
part: 5
status: source-supported
---

<p class="part-kicker part-5">BURGER · VOLUME 1 · PART 5</p>

# PART 5 · SLAM·Localization·Nav2

지도 품질, Initial Pose, Nav2 전제조건, NavigateToPose Action 상태를 독립 Gate로 검증한다.

<div class="part-summary part-5">
  <div><strong>선수 PART</strong><span>PART 4 실물 명령과 시뮬레이션</span></div>
  <div><strong>완료 능력</strong><span>지도·현재 위치·Goal 상태·Cancel을 분리하고 source-supported 기준으로 판정한다.</span></div>
  <div><strong>Lesson</strong><span>4개 · 18–21</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 18
:class-item: lesson-card
**SLAM은 지도 품질과 파일 계약까지 닫는다**

Cartographer 실행, 저속 관측, 지도 품질 판정, YAML·image·SHA-256 보존을 하나의 폐루프로 본다.

[학습하기](../chapters/18-slam은-지도-품질과-파일-계약까지-닫는다.md)
:::

:::{grid-item-card} Lesson 19
:class-item: lesson-card
**Initial Pose는 scan-map 정합으로 판정한다**

RViz 아이콘만 보지 않고 AMCL scan 점이 저장 지도 벽과 위치·yaw 모두 맞는지 확인한다.

[학습하기](../chapters/19-initial-pose는-scan-map-정합으로-판정한다.md)
:::

:::{grid-item-card} Lesson 20
:class-item: lesson-card
**Nav2 Goal은 네 게이트를 모두 통과한 뒤 보낸다**

Lifecycle·TF/Pose·global/local costmap·Action/command ownership을 독립 Gate로 확인한다.

[학습하기](../chapters/20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다.md)
:::

:::{grid-item-card} Lesson 21
:class-item: lesson-card
**NavigateToPose는 모듈형 ament_python 패키지로 만든다**

Goal response·Feedback·Result·Cancel Future를 분리해 Accepted를 terminal success로 오판하지 않는다.

[학습하기](../chapters/21-navigatetopose는-모듈형-ament_python-패키지로-만든다.md)
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
[← PART 4 · 실물 명령과 시뮬레이션](../part-04-hardware-sim/index.md)
:::

:::{grid-item-card} 다음
[PART 6 · 진단·증거·회귀·프로젝트 →](../part-06-evidence/index.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/18-slam은-지도-품질과-파일-계약까지-닫는다
../chapters/19-initial-pose는-scan-map-정합으로-판정한다
../chapters/20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다
../chapters/21-navigatetopose는-모듈형-ament_python-패키지로-만든다
```
