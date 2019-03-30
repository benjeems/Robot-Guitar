#!/usr/bin/env python
 
from time import sleep
import RPi.GPIO as GPIO
sleep(30) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25,False)

GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)

first_time = 0
 
while True:
	sleep (.01)
        if ( GPIO.input(25) == 1 and first_time ==0):
        	execfile("/home/pi/ardunio/bigben/go_strum_Eadgbe.py")
		execfile("/home/pi/ardunio/bigben/go_strum_ebgdaE.py")
		#print "pressed"
		while True:
    			if  GPIO.input(25) == 0 :
				break
	first_time = 0
