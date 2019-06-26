#!/usr/bin/env bash
if [ -x {{ xkeysnail_path.stdout }} ]; then
    exec >> /tmp/xkaysnail.log 2>&1
    xhost +SI:localuser:xkeysnail
    sudo -u xkeysnail DISPLAY=$DISPLAY {{ xkeysnail_path.stdout }} {{ xkeysnail_config_dir }}/config.py &
fi
