import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.output(26, 1)
while True:
  if GPIO.input(19):
      os.system('sudo poweroff')
