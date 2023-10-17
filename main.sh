#!/bin/bash
sudo python3 /home/pi/main.py &
sudo python3 /home/pi/power.py &
if pgrep -f "python3 /home/pi/main.py" &>/dev/null; then
    echo "it is already running"
else
    sudo python3 /home/pi/main.py & 
    sudo python3 /home/pi/power.py &
fi
