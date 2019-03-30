#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

sleep(50)

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
first_time = 1

print first_time
while True:
    sleep(.01)
    # print first_time
    # print GPIO.input(24)
    if GPIO.input(24) == 0 and first_time == 0:
        print "pressed"
        execfile("/home/pi/ardunio/bigben/go_bigben_gong_manual.py")
        while True:
            if GPIO.input(24) == 1:
                break
    first_time = 0
