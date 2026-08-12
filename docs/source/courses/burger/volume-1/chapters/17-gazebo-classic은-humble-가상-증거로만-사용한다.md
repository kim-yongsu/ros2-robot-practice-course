---
title: "17. Gazebo Classic은 Humble 가상 증거로만 사용한다"
source_pdf_page: 21
canonical_language: ko
---

# 17. Gazebo Classic은 Humble 가상 증거로만 사용한다

fake node·Gazebo·실물 Burger가 증명하는 범위를 나누고, Jazzy의 Gazebo Sim 경로와 섞지 않는다.

![Fake node와 Gazebo Classic이 증명하는 범위와 실물 Burger HOLD를 비교하는 도해.](/_static/generated/diagrams/burger/volume-1/figure-18.png)

CMP-17-01 · simulation은 모델·가상 sensor·collision을 검증하지만 OpenCR·battery·실제 wheel을 증명하지 않는다.

| 환경 | 증명 가능한 것 | 증명하지 못하는 것 |
| --- | --- | --- |
| Fake node | 모델·joint·TF·RViz 표현 | sensor·physics·collision |
| Gazebo Classic | spawn·sim time·가상 scan/odom·collision | OpenCR·USB·battery·실제 wheel |
| 실물 Burger | device·firmware·motor·정지 거리 | simulation determinism |

```bash
cd ~/turtlebot3_ws/src
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
source install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

주의  Jazzy는 Gazebo Sim·ros_gz 계열을 사용한다. 이 면은 Humble branch와 Gazebo Classic 계약만 다룬다.
