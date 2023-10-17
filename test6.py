import time
import wiringpi
from time import sleep
import bluetooth
import RPi.GPIO as GPIO
from subprocess import call

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
GPIO.setup(15, 0)
GPIO.setup(11, 0)


#server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#port = 1
#server_socket.bind(('',port))
#server_socket.listen(1)

#client_socket, address = server_socket.accept()


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01
wiringpi.pwmWrite(13,145)
pulse=145

while True:
  
  
  
      setpoint = 145
      if (pulse > setpoint):
        for pulse in range(pulse,setpoint,-1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
        time.sleep(1)
      if (pulse < setpoint):
         for pulse in range(pulse,setpoint,1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
         time.sleep(1)
      
      setpoint = 63
      if (pulse > setpoint):
        for pulse in range(pulse,setpoint,-1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
        time.sleep(1)
      if (pulse < setpoint):
         for pulse in range(pulse,setpoint,1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
         time.sleep(1)
     
      setpoint = 102
      if (pulse > setpoint):
        for pulse in range(pulse,setpoint,-1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
        time.sleep(1)
      if (pulse < setpoint):
         for pulse in range(pulse,setpoint,1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
         time.sleep(1)
  
      setpoint = 192
      if (pulse > setpoint):
        for pulse in range(pulse,setpoint,-1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
        time.sleep(1)
      if (pulse < setpoint):
         for pulse in range(pulse,setpoint,1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
         time.sleep(1)
  
      setpoint = 235
      if (pulse > setpoint):
        for pulse in range(pulse,setpoint,-1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
        time.sleep(1)
      if (pulse < setpoint):
         for pulse in range(pulse,setpoint,1):
           wiringpi.pwmWrite(13,pulse)
           time.sleep(delay_period)
         time.sleep(1)
  
     # setpoint = 212
     # if (pulse > setpoint):
       # for pulse in range(pulse,setpoint,-1):
        #   wiringpi.pwmWrite(13,pulse)
         #  time.sleep(delay_period)
        #time.sleep(1)
     # if (pulse < setpoint):
      #   for pulse in range(pulse,setpoint,1):
       #    wiringpi.pwmWrite(13,pulse)
        #   time.sleep(delay_period)
        # time.sleep(1)
  
