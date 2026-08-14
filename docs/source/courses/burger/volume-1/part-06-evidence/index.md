---
title: PART 6 · 진단·증거·회귀·프로젝트
canonical_language: ko
course_id: burger-v1
part: 6
status: source-supported
---

<p class="part-kicker part-6">BURGER · VOLUME 1 · PART 6</p>

# PART 6 · 진단·증거·회귀·프로젝트

첫 실패 계층, RUN_ID, 회귀시험, 프로젝트 완료 계약을 한 폐루프로 묶는다.

<div class="part-summary part-6">
  <div><strong>선수 PART</strong><span>PART 5 SLAM·Localization·Nav2</span></div>
  <div><strong>완료 능력</strong><span>실패·수정·rollback·증거·인수인계를 같은 실행 조건으로 재현한다.</span></div>
  <div><strong>Lesson</strong><span>4개 · 22–25</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 22
:class-item: lesson-card
**문제는 처음 깨진 계층에서 자른다**

안전부터 base까지 위에서 아래로 확인하고 마지막 PASS와 첫 FAIL을 기록해 무작위 튜닝을 막는다.

[학습하기](../chapters/22-문제는-처음-깨진-계층에서-자른다.md)
:::

:::{grid-item-card} Lesson 23
:class-item: lesson-card
**Evidence Pack은 세 증거층을 한 RUN_ID로 묶는다**

환경·ROS message·물리 관찰을 분리하고 명령·시간·파일 hash로 같은 실행을 재현할 수 있게 보존한다.

[학습하기](../chapters/23-evidence-pack은-세-증거층을-한-run_id로-묶는다.md)
:::

:::{grid-item-card} Lesson 24
:class-item: lesson-card
**한 변수만 바꾸고 같은 시험으로 회귀한다**

수정 전 증거를 보존하고 한 변수만 바꾼 뒤 같은 조건으로 정적·runtime 회귀와 rollback을 닫는다.

[학습하기](../chapters/24-한-변수만-바꾸고-같은-시험으로-회귀한다.md)
:::

:::{grid-item-card} Lesson 25
:class-item: lesson-card
**조별 프로젝트는 재현·안전·증거로 완료한다**

저장 지도에서 A·B·C 목표를 순찰하고 Cancel·STOP, 세 역할, 같은 조건 3회 재현을 하나의 완료 계약으로 묶는다.

[학습하기](../chapters/25-조별-프로젝트는-재현-안전-증거로-완료한다.md)
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
[← PART 5 · SLAM·Localization·Nav2](../part-05-navigation/index.md)
:::

:::{grid-item-card} 다음
[1권 실습 과제 →](../exercises.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/22-문제는-처음-깨진-계층에서-자른다
../chapters/23-evidence-pack은-세-증거층을-한-run_id로-묶는다
../chapters/24-한-변수만-바꾸고-같은-시험으로-회귀한다
../chapters/25-조별-프로젝트는-재현-안전-증거로-완료한다
```
