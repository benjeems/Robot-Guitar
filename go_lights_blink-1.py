#!/usr/bin/env python
import time
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(22,False)
GPIO.output(27,False)

blink_for = 0.08
abort_after = 45

start = time.time()

while True:
	delta = time.time() - start
  	if delta >= abort_after:
    		GPIO.output(22,True)
		GPIO.output(27,True)
		break
	GPIO.output(22,True)
	GPIO.output(27,False)
	sleep(blink_for)
	GPIO.output(22,False)
	GPIO.output(27,True)
	sleep(blink_for)
