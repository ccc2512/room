import webiopi
from webiopi import deviceInstance
import datetime
import time
from time import strftime
import sys

num = 0

while True:
    if (num==2):
        print("begin")
        tmp085 = webiopi.deviceInstance("bmp")
        cel_0 = tmp085.getHectoPascal()
        data_entry = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % cel_0)
        print(data_entry)
        num=0
    num+=1
    time.sleep(1)   # gives CPU some time before looping again
