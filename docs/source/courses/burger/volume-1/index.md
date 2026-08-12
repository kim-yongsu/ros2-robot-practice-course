# 1권 · ROS 2 Humble로 마스터하는 TurtleBot3 Burger

**기준 환경:** Ubuntu 22.04.5 LTS · ROS 2 Humble  
**학습 기체:** TurtleBot3 Burger  
**판정 원칙:** 문서와 정적 검증은 실제 장비 통합시험을 대신하지 않는다.

![Burger 1권의 환경·통신·좌표·실물·자율주행·현장 증거 여섯 단계 학습 경로](/_static/generated/diagrams/burger/volume-1/figure-01.png)

ROS를 처음 접한 독자가 정상 환경의 Burger를 기동하고, 저속 teleop·지도 작성·Localization·기본 Nav2 Goal·계층형 진단을 근거와 함께 설명하도록 안내한다.

```{toctree}
:maxdepth: 2
:caption: 시작하기

reading-guide
learning-map
troubleshooting
exercises
migration-notes
```

```{toctree}
:maxdepth: 1
:caption: 25개 학습 단원

chapters/01-burger로-ros-2의-공통-기준선을-만든다
chapters/02-터미널-linux-생존선을-먼저-확보한다
chapters/03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다
chapters/04-iso-apt-github-workspace의-계보를-분리한다
chapters/05-package-executable-process-node를-구분한다
chapters/06-topic-service-action-parameter를-선택한다
chapters/07-이름보다-type-endpoint-qos-실제-값을-본다
chapters/08-실제-humble-증거-turtlesim과-rqt_graph
chapters/09-실제-humble-증거-c-talker와-python-listener
chapters/10-ros-graph가-안-보이면-층을-나눈다
chapters/11-posestamped는-frame-time-position-orientation-계약이다
chapters/12-tf-edge마다-authority와-시간을-확인한다
chapters/13-urdf와-robot_state_publisher의-책임을-나눈다
chapters/14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다
chapters/15-bringup은-일곱-게이트를-통과한-뒤-실행한다
chapters/16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다
chapters/17-gazebo-classic은-humble-가상-증거로만-사용한다
chapters/18-slam은-지도-품질과-파일-계약까지-닫는다
chapters/19-initial-pose는-scan-map-정합으로-판정한다
chapters/20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다
chapters/21-navigatetopose는-모듈형-ament_python-패키지로-만든다
chapters/22-문제는-처음-깨진-계층에서-자른다
chapters/23-evidence-pack은-세-증거층을-한-run_id로-묶는다
chapters/24-한-변수만-바꾸고-같은-시험으로-회귀한다
chapters/25-조별-프로젝트는-재현-안전-증거로-완료한다
```
