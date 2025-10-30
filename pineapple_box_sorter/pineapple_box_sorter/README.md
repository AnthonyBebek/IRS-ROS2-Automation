# Pineapple Grand Challenge
For those marking this repo is all of the ros2 code the pineapple grand challenge code is pineapple_box_sorter.
```bash
colcon build --packages-select pineapple_box_sorter
ros2 launch pineapple_box_sorter nav_launch.py
```
#### Then in a separate terminal
```bash
ros2 run pineapple_box_sorter hs_waypoint_follower
```
