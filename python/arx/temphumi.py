import datetime
import time
from time import strftime
import sys
import Adafruit_DHT

DHTPIN = 17
num = 0
while True:
    if (num==5):
        humi11, temp11 = Adafruit_DHT.read_retry(11, DHTPIN)
        f = open('/usr/share/webiopi/htdocs/ccc/data_temp11.txt','a')
        data_entry2 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % temp11)
        f.write(data_entry2)
        f.close()
        f = open('/usr/share/webiopi/htdocs/ccc/data_humi11.txt','a')
        data_entry3 = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % humi11)
        f.write(data_entry3)
        f.close()
        print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temp11, humi11))
        num=0
    num+=1
    # gives CPU some time before looping again
    time.sleep(1)
