#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:45:35 2017

start thread to capture photo every second after power on
stop after power off
@author: sjamthe
"""
import threading 
import time
import picamera

e = threading.Event()
camera = picamera.PiCamera()

def take_pics(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        #print('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        #print('event set: %s', event_is_set)
        if event_is_set:
            print('ending thread')
            break
        else:
            print('taking pics')
            camera.capture('/home/pi/hoverpi/web/static/images/test.jpg')


def on():
    t2 = threading.Thread(name='camera', 
                      target=take_pics, 
                      args=(e, 1))
    camera.start_preview()
    t2.start()

def off():
    camera.stop_preview()
    e.set()

on()
print('Waiting before calling Event.set()')
time.sleep(10)
off()
