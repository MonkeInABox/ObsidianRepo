nUWAy_ros2_ws/src/python_nodes/stamped_conversion.py

colcon build --symlink-install source install/setup.bash ros2 run python_nodes stamped_conversion --ros-args -r /joy_cmd_vel:=/cmd_vel # in another terminal ros2 bag record /joy_cmd_vel_stamped -o cmd_vel_stamped_bag