#!/usr/bin/python
from time import sleep

def follow(thefile):
    thefile.seek(0,2)      # Go to the end of the file
    s = 0.2
    while True:
        line = thefile.readline()
        if not line:
            sleep(s)    # Sleep briefly
            if s < 1.0:
                s += 0.00001
            continue
        yield line

logfile = open("/var/log/ufw.log")
loglines = follow(logfile)

for line in loglines:
    if "DPT=" in line:
        DPT = int(line.split("DPT=")[1].split(" ")[0])
        if DPT <= 1024: 
            execfile("/home/pi/ardunio/bigben/go_strum_E.py")    
            print "###### LOW PORT < 1024"
	    print DPT
        else:
            execfile("/home/pi/ardunio/bigben/go_strum_e.py")    
            print "###### HIGH PORT > 1024"
	    print DPT
    print line,
