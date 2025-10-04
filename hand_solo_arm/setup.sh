#!/bin/bash
set -e # exit on first error

WORKSPACE=~/ros2_ws
PKG_NAME=hand_solo_arm

echo ">>> Building $PKG_NAME inside $WORKSPACE"
cd $WORKSPACE

colcon build --packages-select $PKG_NAME

echo ">>> Sourcing workspace..."
source /opt/ros/humble/setup.sh
source install/local_setup.bash

# Launch the package
ros2 run hand_solo_arm hs_pick_place


