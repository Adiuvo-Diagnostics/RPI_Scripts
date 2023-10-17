import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


GPIO.setup(22, 0)
GPIO.setup(18, 0)
GPIO.setup(16, 0)
#GPIO.setup(15, 0)
GPIO.setup(11, 0)

while True:

  GPIO.output(22, 1)
  time.sleep(2)
  GPIO.output(22, 0)

  GPIO.output(18, 1)
  time.sleep(2)
  GPIO.output(18, 0)

  GPIO.output(16, 1)
  time.sleep(2)
  GPIO.output(16, 0)

#  GPIO.output(15, 1)
 # time.sleep(2)
 # GPIO.output(15, 0)

  GPIO.output(11, 1)
  time.sleep(2)
  GPIO.output(11, 0)

  GPIO.output(22, 0)
  GPIO.output(18, 0)
  GPIO.output(16, 0)
  #GPIO.output(15, 0)
  GPIO.output(11, 0)
  time.sleep(5)



