#!/usr/bin/python
import glob
import serial
from time import sleep , strftime

arduino_serial_id = glob.glob("/dev/ttyACM*")[0]
ser = serial.Serial(arduino_serial_id , 9600)

wait = .75
wait_longer = 1.0  # Can play with this value so to give a more nrandom timing effect
wait_gong = 2.0
# Quting from http://en.wikipedia.org/wiki/Big_Ben
#One of the requirements for the clock was that the first stroke of the hour bell should register the time, correct to within one second per day. So, at twelve o'clock, for example, it is the first of the twelve hour-bell strikes that signifies the hour. 
# If this script is run by cronjob at start of every hour, calculate how long to wait before beginning the chime sequence (ie for the next hour) 
#must_sleep_for =(60 - (7 * wait) - (1 * wait_longer) - (1 * wait_gong) - 1.25)
#sleep(must_sleep_for)
gongs = int(strftime("%I").lstrip("0")) + 1 # This is the number of the _next_ hour, to be used later on  hour gongs.
if gongs == 13:         # special case where the current hour is 12, need to make a acorrection for 1pm 
    gongs = 1
gongs_24h = int(strftime("%H").lstrip("0")) + 1   # need this for later when working out what hours not to chime whilst one sleeps
day_of_week = int(strftime("%w"))

def chime():
        ser.write('4')
        sleep(wait)
        ser.write('3')
        sleep(wait_longer)
        ser.write('1')
        sleep(wait)
        ser.write('2')
        sleep(wait)
        sleep(wait)

        ser.write('2')
        sleep(wait)
        ser.write('3')
        sleep(wait)
        ser.write('4')
        sleep(wait)
        ser.write('3')

        sleep(wait_gong)
        for i in range(0,gongs):        # Run loop 'gong' times
                ser.write('0')          # The FIRST of these gongs signifies the exact change of hour 
                sleep(wait_gong)


chime() 

#if day_of_week > 0 and day_of_week < 6 and gongs_24h > 5 and gongs_24h < 21: # don't gong till 6am on weekdays
#	chime() 
#elif (day_of_week == 0 or day_of_week == 6) and gongs_24h > 9 and gongs_24h < 21: #don't gong till 10am in weekends
#	chime()

