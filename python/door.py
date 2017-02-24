#/usr/bin/python
#utf-8

import RPi.GPIO as GPIO
import time
import datetime
from time import strftime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

irdd_pin = 18
rled_pin = 7

vkl      = True
otkl     = False
curr_val = 0

GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(door_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(door_pin,GPIO.IN,pull_up_down=GPIO.PUD_OFF) 

GPIO.setup(irdd_pin,GPIO.IN)
GPIO.setup(rled_pin,GPIO.OUT)

try:
   while True:
      if GPIO.input(irdd_pin):
         GPIO.output(rled_pin,vkl)
         if curr_val != 1:
            f = open('/usr/share/webiopi/htdocs/ccc/txt/data_irdd.txt','a')
            log_entry = "{0},1\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f")
            f.write(log_entry)
            f.close()
            curr_val = 1
         #print('IRDD up')
      else:
         GPIO.output(rled_pin,otkl)
         if curr_val != 0:
            f = open('/usr/share/webiopi/htdocs/ccc/txt/data_irdd.txt','a')
            log_entry = "{0},0\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f")
            f.write(log_entry)
            f.close()
            curr_val = 0
         #print('IRDD down')
      time.sleep(1)

except KeyboardInterrupt():
   GPIO.output(rled_pin,otkl)
   GPIO.cleanup()
