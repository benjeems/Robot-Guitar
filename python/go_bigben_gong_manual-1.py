#!/usr/bin/python
import glob
import serial
from time import sleep, strftime

arduino_serial_id = glob.glob("/dev/ttyACM*")[0]
ser = serial.Serial(arduino_serial_id, 9600)
# Can play with these value so to give a more random timing effect
wait = .75
wait_longer = 1.0
wait_gong = 2.0
# Quting from http://en.wikipedia.org/wiki/Big_Ben
# One of the requirements for the clock was that the first stroke of the hour
# bell should register the time, correct to within one second per day. So,
# at twelve o'clock, for example, it is the first of the twelve hour-bell
# strikes that signifies the hour.
# If this script is run by cronjob at start of every hour, calculate how long
# to wait before beginning the chime sequence (ie for the next hour)
# must_sleep_for =(60 - (7 * wait) - (1 * wait_longer) - (1 * wait_gong) - 1.25)
# sleep(must_sleep_for)
# This is the number of the _next_ hour, to be used later on  hour gongs.
gongs = int(strftime("%I").lstrip("0")) + 1
# special case where the current hour is 12, need to make a acorrection for 1pm
if gongs == 13:
    gongs = 1
day_of_week = int(strftime("%w"))
gongs_24h = int(strftime("%H").lstrip("0")) + 1


def chime():
    """ Chime Big Ben at the changing of the hour """

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
    # Run loop 'gong' times
    for i in range(0, gongs):
        # The FIRST of these gongs signifies the exact change of hour
        ser.write('0')
        sleep(wait_gong)


chime()
