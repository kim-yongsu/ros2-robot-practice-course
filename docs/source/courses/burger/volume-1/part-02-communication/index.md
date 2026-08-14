---
title: PART 2 · ROS 2 통신과 실행 증거
canonical_language: ko
course_id: burger-v1
part: 2
status: source-supported
---

<p class="part-kicker part-2">BURGER · VOLUME 1 · PART 2</p>

# PART 2 · ROS 2 통신과 실행 증거

실행 단위와 interface를 구분하고 이름이 아니라 type·endpoint·QoS·실제 message로 통신을 판정한다.

<div class="part-summary part-2">
  <div><strong>선수 PART</strong><span>PART 1 환경 기준선</span></div>
  <div><strong>완료 능력</strong><span>Package부터 Node까지의 실행 관계와 Topic·Service·Action·Parameter의 계약을 증거로 설명한다.</span></div>
  <div><strong>Lesson</strong><span>5개 · 05–09</span></div>
</div>

## 이 PART의 학습 경로

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lesson-card-grid

:::{grid-item-card} Lesson 05
:class-item: lesson-card
**Package·Executable·Process·Node를 구분한다**

배포 묶음, 실행 진입점, OS process, ROS graph Node를 각각 다른 명령으로 확인한다.

[학습하기](../chapters/05-package-executable-process-node를-구분한다.md)
:::

:::{grid-item-card} Lesson 06
:class-item: lesson-card
**Topic·Service·Action·Parameter를 선택한다**

데이터 빈도만이 아니라 응답, 진행 상태, 취소, 설정 소유권을 기준으로 ROS 2 interface를 선택한다.

[학습하기](../chapters/06-topic-service-action-parameter를-선택한다.md)
:::

:::{grid-item-card} Lesson 07
:class-item: lesson-card
**이름보다 type·endpoint·QoS·실제 값을 본다**

토픽 이름의 존재를 통신 증거로 확대하지 않고 endpoint type·QoS 호환성과 실제 message를 순서대로 확인한다.

[학습하기](../chapters/07-이름보다-type-endpoint-qos-실제-값을-본다.md)
:::

:::{grid-item-card} Lesson 08
:class-item: lesson-card
**실제 Humble 증거 — turtlesim과 rqt_graph**

Publisher → Topic → Subscriber 연결과 simulator 상태 변화를 함께 보되 rqt_graph가 증명하지 못하는 범위를 남긴다.

[학습하기](../chapters/08-실제-humble-증거-turtlesim과-rqt_graph.md)
:::

:::{grid-item-card} Lesson 09
:class-item: lesson-card
**실제 Humble 증거 — C++ talker와 Python listener**

서로 다른 구현 언어가 같은 interface contract로 통신한 원본 로그의 sequence와 timestamp를 짝지어 검증한다.

[학습하기](../chapters/09-실제-humble-증거-c-talker와-python-listener.md)
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
[← PART 1 · 환경 기준선](../part-01-environment/index.md)
:::

:::{grid-item-card} 다음
[PART 3 · 발견·좌표·TF·URDF →](../part-03-frames/index.md)
:::

::::

```{toctree}
:hidden:
:maxdepth: 1

../chapters/05-package-executable-process-node를-구분한다
../chapters/06-topic-service-action-parameter를-선택한다
../chapters/07-이름보다-type-endpoint-qos-실제-값을-본다
../chapters/08-실제-humble-증거-turtlesim과-rqt_graph
../chapters/09-실제-humble-증거-c-talker와-python-listener
```
