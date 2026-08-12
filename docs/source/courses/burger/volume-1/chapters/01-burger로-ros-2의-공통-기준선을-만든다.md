---
title: "1. Burger로 ROS 2의 공통 기준선을 만든다"
source_pdf_page: 5
canonical_language: ko
---

# 1. Burger로 ROS 2의 공통 기준선을 만든다

TurtleBot3 Burger는 목적이 아니라 ROS 2의 환경·통신·좌표·실물·자율주행·유지보수 계약을 한 번에 확인하는 기준 플랫폼이다.

![환경, 통신, 좌표, 실물, 자율주행, 실무의 여섯 단계가 앞 단계의 정상 결과를 다음 단계 입력으로 사용하는 구조](/_static/generated/diagrams/burger/volume-1/figure-02.png)

1권 Burger 학습 경로

| 독자 | 이 책으로 할 수 있어야 하는 일 |
| --- | --- |
| 학생 | 명령을 따라 하고 정상 결과·STOP 조건·첫 진단을 설명 |
| 교사 | 실습 순서와 실패 주입 지점을 통제 |
| 신입 | 환경·그래프·TF·하드웨어·Nav2 계층을 분리 진단 |
| 베테랑 | 명령·인터페이스·증거 위치를 빠르게 재확인 |

판정 원칙  GUI가 열렸거나 토픽 이름이 보였다는 이유만으로 PASS하지 않는다. 실제 값·물리 반응·최종 상태·증거까지 확인한다.

| 종료 게이트 | PASS 증거 | HOLD 경계 |
| --- | --- | --- |
| Graph·TF | type·endpoint·TF chain | 이름만 존재 |
| 실물·지도 | 정지·scan·odom·map 파일 | simulator만 확인 |
| Nav2·진단 | Result·실패 재현·복구 기록 | Goal 전송만 확인 |
