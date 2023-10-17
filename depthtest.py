
import board
import busio 
import adafruit_vl6180x 
import RPi.GPIO as GPIO
import time
from time import sleep
import numpy as np
sensors=0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18 ,GPIO.OUT)


i2c = busio.I2C(board.SCL, board.SDA)
GPIO.output(18, GPIO.HIGH)
#f = open('gcode.csv','w')
for num in range(1, 50, 1):
  sensor=adafruit_vl6180x.VL6180X(i2c)
  
 # print(format(sensor.range))
  print('Range:{0}mm'.format(sensor.range))
  sensors+=int(format(sensor.range))
  f.write(str(format(sensor.range)) + '\n')
GPIO.output(18,GPIO.LOW)
average=sensors/50
print('Averaged o/p:',average)







