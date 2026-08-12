---
title: "5. Package·Executable·Process·Node를 구분한다"
source_pdf_page: 9
canonical_language: ko
---

# 5. Package·Executable·Process·Node를 구분한다

파일 묶음과 실행 진입점, 운영체제 process, ROS graph의 Node는 서로 다른 단위다. 같은 이름처럼 보여도 확인 명령이 다르다.

![demo_nodes_cpp package, talker executable, 운영체제 process, /talker Node가 순서대로 연결되는 네 단계 도해](/_static/generated/diagrams/burger/volume-1/figure-06.png)

Package에서 Node까지의 실행 관계

| 단위 | 무엇인가 | 확인 명령 |
| --- | --- | --- |
| Package | 소스·설정·실행 파일의 배포 묶음 | ros2 pkg list·prefix |
| Executable | package가 설치한 실행 진입점 | ros2 pkg executables |
| Process | OS가 PID·자원을 관리하는 실행 단위 | ps·top·systemctl |
| Node | ROS graph의 통신·parameter 주체 | ros2 node list·info |

```bash
ros2 pkg executables demo_nodes_cpp
ros2 run demo_nodes_cpp talker
ros2 node list
ros2 node info /talker
ps -ef | grep '[t]alker'
```

주의  Executable 이름과 Node 이름은 같을 수도 다를 수 있다. component container처럼 한 process가 여러 Node를 품을 수도 있다.
