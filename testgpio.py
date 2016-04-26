#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pygame
from pygame.locals import *
from subprocess import Popen 
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
SWITCH = 21
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

RELAY = 18
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, False)


def timedef_sec(dt):
  return dt.total_seconds()

def check_but_state():
  start_time = datetime.now()
  while (timedef_sec(datetime.now() - start_time) <= 0.5):
    if (not GPIO.input(SWITCH)):
      return False
  return True  
  
"""  
while 1:
  print (check_but_state())
  print (GPIO.input(SWITCH))
"""
  
while 1:
  print("On")
  GPIO.output(RELAY, True)
  pygame.time.delay(3000)
  print("Off")
  GPIO.output(RELAY, False)
  pygame.time.delay(1000)

