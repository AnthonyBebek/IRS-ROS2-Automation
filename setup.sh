#!/bin/bash
read -p "Do you want to install dependencies? [y/n]: " choice

case $choice in
  y|Y)
    echo "Installing dependencies..."
    sudo apt update
    sudo apt install -y ros-humble-rqt-tf-tree
    ;;
  n|N)
    echo "Skipping dependency installation."
    ;;
  *)
    echo "Invalid choice. Doing nothing."
    ;;
esac

echo ""
echo "Chose pkg to run:"
echo "1) pa_warehouse_status"
echo "2) hand_solo_virtual_nav"
read -p "Enter your choice [1-2]: " choice

case $choice in
  1)
    echo "Running pa_warehouse_status"
    bash ./pa_warehouse_status/setup.sh
    ;;
  2)
    echo "Running hand_solo_virtual_nav"
    bash ./hand_solo_virtual_nav/setup.sh
    ;;
  *)
    echo "Invalid option, please try again."
    ;;
esac
