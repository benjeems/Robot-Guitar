#!/usr/bin/python
import glob 
import serial
from time import sleep

arduino_serial_id = glob.glob("/dev/ttyACM*")[0]
ser = serial.Serial(arduino_serial_id, 9600)
#sleep(1)
#ser.setDTR(level=0)
#ser.dsrdtr=False
#ser.setDTR(level=False)
#sleep(1)
#ser.write('5')
#sleep(.1)
ser.write('4')
sleep(.1)
ser.write('3')
sleep(.1)
ser.write('2')
sleep(.1)
ser.write('1')
sleep(.1)
ser.write('0')
sleep(.1)
