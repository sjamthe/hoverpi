#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:02:32 PDT 2019

hoverpi: control hoverboard over serial
@author: sjamthe
"""

import serial
import sys
import io
import os

cmd_map = {
    'on': 'on',
    'off': 'off',
    'left': 'l 1',
    'right': 'r 1',
    'forward': 'f 10',
    'backward': 'b 5',
}

def hovercmd(cmdstr):
    tty='/dev/ttyACM0'
    with serial.Serial(tty, 500000, timeout=1) as ser:
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1))
        sio.write(cmd_map[cmdstr] + '\n')
        sio.flush()
        #debug
        #line = sio.read(-1)
        #print (line)

def cmd_on():
    hovercmd('on')

def cmd_off():
    hovercmd('off')

#testing
#cmd_on()
#sleep(10)
#hovercmd('left')
#cmd_off()
