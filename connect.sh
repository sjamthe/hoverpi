#!/bin/sh

# connect.sh

# Usage:
# $ connect.sh <device> <port speed>
# Example: connect.sh /dev/ttyS0 9600

# Set up device
#stty -F $1 $2
tty=/dev/ttyACM0
baud=500000
stty -F $tty $baud

# Let cat read the device $1 in the background
cat $tty &

# Capture PID of background process so it is possible to terminate it when done
bgPid=$!

# Read commands from user, send them to device $1
while read cmd
do
   echo "$cmd" 
done > $tty

# Terminate background read process
kill $bgPid
