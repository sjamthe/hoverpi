#!/bin/bash
exit_script() {
    echo "sending kill to child process (mjpg-streamer)"
    trap - SIGINT SIGTERM # clear the trap
    kill -- -$$ # Sends SIGTERM to child/sub processes
}

trap exit_script SIGINT SIGTERM

APP_HOME='/home/pi/src/hoverpi/web2'
export LD_LIBRARY_PATH=$APP_HOME/../mjpg-streamer-experimental
$APP_HOME/../mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w $APP_HOME/../mjpg-streamer-experimental/www" -i "input_raspicam.so -x 400 -y 400 -fps 30 -ex night" &
env FLASK_APP=$APP_HOME/control.py flask run --host=0.0.0.0
kill %1
cd -
