#!/bin/bash
set -e # exit on first error

WORKSPACE=~/ros2_ws
PKG_NAME=hand_solo_virtual_nav
LAUNCH_FILE=mapping_launch.py

echo ">>> Building $PKG_NAME inside $WORKSPACE"
cd $WORKSPACE

colcon build --packages-select $PKG_NAME

echo ">>> Sourcing workspace..."
source /opt/ros/humble/setup.sh
source install/local_setup.bash

# Running rqt_tf_tree
echo ">>> Running rqt_tf_tree"
ros2 run rqt_tf_tree rqt_tf_tree

# Launch the package
echo ">>> Launching $PKG_NAME with $LAUNCH_FILE..."
ros2 launch $PKG_NAME $LAUNCH_FILE


