Restart
Boot into: `Ubuntu 22`
```
cd ./Unity/Exec
./REVSIMv1.3.1.x86_64

cd ./Unity/REVSIM_ros2_ws
ros2 launch robot_description controller_js1.launch.py
# if this doesnt work:
ros2 launch robot_description controller.launch.py

ros2 bag record /nn_cmd_vel

ros2 bag record /lidar_localisation/front/cloud

ros2 bag record /lidar_localisation/rear/cloud
```