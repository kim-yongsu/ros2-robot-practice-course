---
title: "15. bringup은 일곱 게이트를 통과한 뒤 실행한다"
source_pdf_page: 19
canonical_language: ko
---

# 15. bringup은 일곱 게이트를 통과한 뒤 실행한다

SSH가 된다는 사실만으로 bringup 준비를 합격시키지 않고 첫 FAIL 계층에서 멈춘다.

![안전, 전원, device, network, ROS environment, model, launch 순서의 Go/No-Go.](/_static/generated/diagrams/burger/volume-1/figure-16.png)

GATE-15-01 · Remote PC와 SBC의 책임을 분리하고, 장치 기본값은 실제 port와 LDS 모델로 재확인한다.

| 게이트 | PASS 기준 | FAIL이면 |
| --- | --- | --- |
| 안전·전원 | 넓은 바닥·정지 담당·배터리·케이블 | 전원 차단 후 재배치 |
| 장치 | OpenCR·LDS port와 권한 확인 | 케이블·udev·firmware |
| 네트워크 | IP·SSH·multicast 경로 | ROS 이전 연결 복구 |
| ROS 계약 | Humble·Domain·RMW·burger·LDS_MODEL | 환경변수·source 교정 |
| bringup | node·topic·TF·log가 함께 정상 | 첫 오류에서 원인 분리 |

```bash
# Remote PC → SBC
ssh ubuntu@<SBC_IP>
# TurtleBot3 SBC
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py
```

주의  /dev/ttyACM0과 /dev/ttyUSB0은 Humble launch의 기본값이다. 실제 장비의 영구 고정값으로 단정하지 않는다.
