# 트러블슈팅 빠른 입구

문제를 한꺼번에 고치지 않는다. 안전부터 아래 계층으로 내려가며 **첫 FAIL**을 찾는다.

1. 안전·전원·물리 STOP
2. IP·USB·SBC·장치 권한
3. ROS 환경·source·Domain·RMW
4. graph의 name·type·endpoint·QoS
5. TF·timestamp·Fixed Frame
6. SLAM·Localization·Nav2 lifecycle·costmap
7. `/cmd_vel` publisher와 실제 base·wheel 반응

`/cmd_vel`이 존재하는 것, 값이 흐르는 것, 바퀴가 실제로 움직이는 것은 서로 다른 증거다. Cancel 응답은 물리 E-stop 성공을 뜻하지 않는다.
