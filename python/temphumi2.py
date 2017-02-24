import datetime
import time
from time import strftime
import sys
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

DataPin = 24
SCKPin  = 23

with SHT1x(DataPin, SCKPin, gpio_mode=GPIO.BCM) as sensor:
    tempSHT = sensor.read_temperature()
    humiSHT = sensor.read_humidity(tempSHT)
    #sensor.calculate_dew_point(tempSHT,humiSHT)
f = open('/usr/share/webiopi/htdocs/ccc/txt/data_tempSHT.txt','a')
data_entry2 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % tempSHT)
f.write(data_entry2)
f.close()
f = open('/usr/share/webiopi/htdocs/ccc/txt/data_humiSHT.txt','a')
data_entry3 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % humiSHT)
f.write(data_entry3)
f.close()
