#!/usr/bin/env python3

import picamera
from time import sleep

camera = picamera.PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/hoverpi/web/static/images/test.jpg')
#camera.stop_preview()
