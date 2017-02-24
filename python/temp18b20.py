import webiopi
from webiopi import deviceInstance
import datetime
import time
from time import strftime
import sys

DHTPIN = 17
num = 0
cel_2 = 30
while True:
    if (num==2):
        print("begin")
        tmp0 = webiopi.deviceInstance("temp0")
        cel_0 = tmp0.getCelsius()
        cel_0 = 21
        if cel_0 != cel_2:
            data_entry = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % cel_0)
            print(data_entry)
            cel_2 = cel_0
        num=0
    num+=1
    time.sleep(1)   # gives CPU some time before looping again
