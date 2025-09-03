#!/bin/bash
set -e  # exit on first error

WORKSPACE=~/ros2_ws
PKG_NAME=pa_warehouse_status
NODE_NAME=gossip_PLC

echo ">>> Building $PKG_NAME inside $WORKSPACE"
cd $WORKSPACE

colcon build --packages-select $PKG_NAME

echo ">>> Sourcing workspace..."
source /opt/ros/humble/setup.sh
source install/local_setup.bash

# Run the package
echo ">>> Running $PKG_NAME..."
ros2 run pa_warehouse_status $NODE_NAME
