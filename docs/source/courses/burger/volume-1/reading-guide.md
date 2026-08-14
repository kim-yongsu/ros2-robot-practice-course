---
title: 읽는 법과 판정 원칙
canonical_language: ko
course_id: burger-v1
status: source-supported
---

# 읽는 법과 판정 원칙

명령을 따라 하는 것으로 끝내지 않고 **어디서 실행하고, 무엇을 보고, 무엇이면 멈추며, 무엇을 증거로 남기는지**를 함께 확인한다.

## 화면의 공통 구조

| 구역 | 읽는 방법 |
| --- | --- |
| 학습 목표 | 이 Lesson을 마친 뒤 설명·실행할 수 있어야 하는 것 |
| 선수 조건 | 없으면 다음 결과를 만들지 않고 HOLD할 입력 |
| 실행 | source-supported 명령 또는 비교·판정 작업 |
| 예상 결과 | 원문이 제시한 정상 조건이며 가짜 출력 로그가 아님 |
| 관찰 | 이름·GUI와 실제 값·물리 반응을 구분하는 지점 |
| PASS / HOLD / FAIL | 통과, 증거 부족, 잘못된 판정 경계 |
| STOP | 안전·복구를 위해 즉시 중단할 조건 |
| 증거 | 다음 Lesson과 회귀시험에 다시 사용할 자료 |

## VERIFY

- OS·ROS_DISTRO·Domain·RMW·기체 모델을 현재 shell에서 확인한다.
- Node·Topic 이름뿐 아니라 type·endpoint·QoS·실제 message를 확인한다.
- 실물에서는 command와 device·wheel 반응·정지를 별도 증거로 둔다.
- Nav2에서는 Goal 전송, Accepted, terminal Result를 서로 다른 상태로 기록한다.

## STOP

정지 불가·예상 밖 방향·발열·반복 disconnect·전원/케이블 위험이 있으면 실습을 즉시 멈춘다. software stop과 Action Cancel은 물리 비상정지를 대신하지 않는다.

## HOLD

다음은 실패가 아니라 **증거가 아직 없는 상태**다.

- simulator만 확인했고 실물 결과가 없음
- 이름은 보이나 실제 message가 없음
- 지도 파일은 생겼지만 구조 품질을 확인하지 않음
- Goal은 보냈으나 terminal Result가 없음
- 정적 test는 통과했으나 Humble·DDS·Nav2·실물 통합을 실행하지 않음

## 진행률

완료 표시는 브라우저 `localStorage`의 `ros2-course:burger:v1:progress` 키에만 저장된다. 서버 전송·로그인·추적은 없으며, JavaScript가 꺼져도 전체 본문과 링크를 사용할 수 있다.

## 이전 / 다음 학습

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Burger 1권 시작하기](start.md)
:::

:::{grid-item-card} 다음 학습 →
[6단계 학습 지도](learning-map.md)
:::

::::
