#!/bin/bash
echo "Enter to update flatpak and update"

meh=""
read meh
sudo apt upgrade -y && flatpak upgrade -y
