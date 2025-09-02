#!/bin/bash
set -e  # exit on first error

WORKSPACE=~/ros2_ws
PKG_NAME=pa_warehouse_status

echo ">>> Building $PKG_NAME inside $WORKSPACE"
cd $WORKSPACE

colcon build --packages-select $PKG_NAME

echo ">>> Sourcing workspace..."
source install/setup.bash

# Run the package
echo ">>> Running $PKG_NAME..."
