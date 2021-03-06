import webiopi
import datetime
import time
import sys
from webiopi import deviceInstance
from time import strftime

GPIO = webiopi.GPIO

LIGHT = 21 # GPIO pin for LIGHT

HOUR_OFF  = 8
MIN_OFF   = 5

HOUR_ON   = 18
MIN_ON    = 35

celsius_0 = 0,0
cel_0     = 0,0
num       = 1

# setup function is automatically called at WebIOPi startup
def setup():
   # set the GPIO used by the light to output
   GPIO.setFunction(LIGHT,GPIO.OUT)
   
@webiopi.macro
def getBMP085Press():
   global pressure_085
   press0 = webiopi.deviceInstance("bmp")
   pressure_085 = press0.getHectoPascal()  # получение давления
   pressure_085 = pressure_085*0.75        # перевод в мм.рт.ст
   print (pressure_085)
   return "%.2f" % pressure_085 # возврат данных давления в HTML с округлением до сотых

@webiopi.macro
def getBMP085Temp():
   global celsius_085
   tmp085 = webiopi.deviceInstance("bmp")
   celsius_085 = tmp085.getCelsius()  # получение температуры
   print (celsius_085)
   return "%.2f" % celsius_085 # возврат данных температуры в HTML с округлением до сотых

@webiopi.macro
def getTmp0():
   global celsius_0
   tmp0 = webiopi.deviceInstance("temp0")
   celsius_0 = tmp0.getCelsius()  # получение температуры
   print (celsius_0)
   return "%.2f" % celsius_0 # возврат данных температуры в HTML с округлением до сотых

@webiopi.macro
def fTime():
   now = datetime.datetime.now()
   return "{0}".format(strftime("%H:%M"))

@webiopi.macro
def fDate():
   now = datetime.datetime.now()
   return "{0}".format(strftime("%d.%m.%Y"))

@webiopi.macro
def fLight():
   if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
      mLight = "ON"
   else:
      mLight = "OFF"
   return mLight

def loop():
   global cel_0
   global num
   tmp0 = webiopi.deviceInstance("temp0")
   tmp085       = webiopi.deviceInstance("bmp")
   cnt = 0
   allTemp      = 0
   allTemp085   = 0
   allTPress085 = 0
   while cnt<60:
      # retrieve current datetime
      now = datetime.datetime.now()
      mOffSecond = HOUR_OFF * 60 * 60 + MIN_OFF * 60
      mOnSecond  = HOUR_ON  * 60 * 60 + MIN_ON  * 60
      mNumSecond = now.hour * 60 * 60 + now.minute * 60 + now.second
      if mNumSecond >= mOffSecond and mNumSecond <= mOnSecond:
         GPIO.digitalWrite(LIGHT,GPIO.LOW)
      else:
         GPIO.digitalWrite(LIGHT,GPIO.HIGH)
      #read temp 
      oneTemp     = tmp0.getCelsius()
      oneTemp085  = tmp085.getCelsius()
      onePress085 = tmp085.getHectoPascal()
      onePress085 = onePress085 * 0.75
      allTemp     = allTemp + oneTemp
      allTemp085  = allTemp085 + oneTemp085
      allPress085 = allTPress085 + onePress085
      time.sleep(5)
      cnt+=1
   avrTemp     = allTemp / 60
   avrTemp085  = allTemp085 / 60
   avrPress085 = allPress085 / 60
   f = open('/usr/share/webiopi/htdocs/ccc/txt/data_18B20.txt','a')
   data_entry = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % avrTemp)
   f.write(data_entry)
   f.close()
   f = open('/usr/share/webiopi/htdocs/ccc/txt/data_tempBMP085.txt','a')
   data_entry = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % avrTemp085)
   f.write(data_entry)
   f.close()
   f = open('/usr/share/webiopi/htdocs/ccc/txt/data_pressBMP085.txt','a')
   data_entry = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),"%.2f" % allPress085)
   f.write(data_entry)
   f.close()

# destroy function is called at WebIOPi shutdown
def destroy():
   GPIO.digitalWrite(LIGHT, GPIO.LOW)

