#!/bin/bash
set -e # exit on first error

WORKSPACE=~/ros2_ws
PKG_NAME=pineapple_box_sorter
LAUNCH_FILE=nav_launch.py

echo ">>> Building $PKG_NAME inside $WORKSPACE"
cd $WORKSPACE

colcon build --packages-select $PKG_NAME

echo ">>> Sourcing workspace..."
source /opt/ros/humble/setup.sh
source install/local_setup.bash

# Launch the package
echo ">>> Launching $PKG_NAME with $LAUNCH_FILE..."
ros2 launch $PKG_NAME $LAUNCH_FILE


