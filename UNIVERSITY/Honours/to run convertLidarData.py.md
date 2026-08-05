```
colcon build --packages-select python_nodes_interfaces

source ./install/setup.bash

source /opt/ros/humble/setup.bash

# ensure that the path has been changed in the python file
python3 convertLidarData.py
```