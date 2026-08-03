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

NEW
```
cd ./Unity/Exec
./REVSIMv1.3.1.x86_64

# new terminal
cd ~/nUWAy_ros2_ws-nuway3_humble_dev/
source install/setup.bash
ros2 run python_nodes stamped_conversion

# new terminal
cd ~/Unity/REVSIM_ros2_ws
source ./install/setup.bash
ros2 launch robot_description controller_js1.launch.py
# if this doesnt work:
ros2 launch robot_description controller.launch.py

ros2 bag record -a -o ~/media/sim/BCC8-9211 -s mcap
```