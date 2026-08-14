---
title: 1권 실습 과제
canonical_language: ko
course_id: burger-v1
status: source-supported
---

# 1권 실습 과제

실제 출력과 실물 PASS를 문서가 대신 만들지 않는다. 각 과제는 수행 증거가 없으면 `HOLD`다.

## 과제 1 · 환경 기준선

Remote PC와 SBC에서 OS·ROS_DISTRO·Domain·RMW·workspace source 순서를 수집하고 한 변수만 다른 비교표를 만든다.

## 과제 2 · 통신 증거

하나의 Topic을 list → endpoint → interface → message → rate 순서로 조사하고 각 단계가 증명하는 것과 못하는 것을 적는다.

## 과제 3 · TF와 model 책임

map→odom→base_link→base_scan chain의 authority·시간과 URDF·joint_states·robot_state_publisher 책임을 분리한다.

## 과제 4 · 실물·simulation 경계

`/cmd_vel` Publisher·Message·Device·물리 반응을 한 표에 놓고 Gazebo가 대신 증명할 수 없는 항목을 HOLD로 표시한다.

## 과제 5 · Nav2 Gate

Lifecycle·TF/Pose·Costmaps·Action/command/STOP 네 Gate를 채우고 Goal 전송 여부를 판정한다.

## 과제 6 · Evidence Pack과 회귀

RUN_ID 하나에 환경·ROS·물리 evidence를 묶고 한 변수 변경 전후를 같은 조건으로 재시험한다.

## 최종 프로젝트 계약

[Lesson 25](chapters/25-조별-프로젝트는-재현-안전-증거로-완료한다.md)의 준비·임무·안전·재현·포트폴리오 다섯 계층을 사용한다. simulator 3회·실물 3회·물리 STOP·팀 역할은 실제 증거가 들어오기 전까지 HOLD다.
