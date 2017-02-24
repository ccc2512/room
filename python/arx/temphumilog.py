import datetime
import time
from time import strftime
import sys
import Adafruit_DHT

DHTPIN = 12

humi22, temp22 = Adafruit_DHT.read_retry(22, DHTPIN)
f = open('/usr/share/webiopi/htdocs/ccc/data_temp22.txt','a')
data_entry2 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % temp22)
f.write(data_entry2)
f.close()
f = open('/usr/share/webiopi/htdocs/ccc/data_humi22.txt','a')
data_entry3 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % humi22)
f.write(data_entry3)
f.close()
#print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temp22, humi22))
