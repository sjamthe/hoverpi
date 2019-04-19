#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:45:35 2017

hoverpi: control hoverboard over serial
	 take picture every second from on to off
@author: sjamthe
"""

import serial
import sys
import io
import os
import threading
import picamera
from time import sleep
from shutil import copyfile

#should be in init
img = '/home/pi/hoverpi/web/static/images/test.jpg'
dest = '/home/pi/hoverpi/web/data/'

e = threading.Event()

def take_pics(e, t):
    camera = picamera.PiCamera()
    camera.start_preview()
    i=0
    while not e.isSet():
        event_is_set = e.wait(t) #secs to wait before taking pic
        if event_is_set:
            camera.close()
            break #exit if off is called
        else:
            #print("talking pic %s",i);
            camera.capture(img)
            i+=1

def saveimage(cmdstr):
    cmd0 = cmdstr.split()[0]
    if(cmd0 == 'on' or cmd0 == 'off'):
        return
    destdir=dest + cmd0 
    filecnt = len(os.listdir(destdir))
    destfile=destdir + '/' + cmdstr + '-' + filecnt + '.jpg'
    copyfile(img,destfile)

def cmd(cmdstr):
    tty='/dev/ttyACM0'
    saveimage(cmdstr)
    with serial.Serial(tty, 500000, timeout=10) as ser:
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        sio.write(cmdstr + '\n')
        sio.flush()

def cmd_on():
    t1 = threading.Thread(name='camera',
                  target=take_pics,
                  args=(e, 1))
    t1.start()
    cmd('on')

def cmd_off():
    e.set()
    cmd('off')

#cmd_on()
#sleep(10)
#cmd_off()
