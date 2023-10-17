import time
import wiringpi
from time import sleep
from bluetooth import *
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

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01
wiringpi.pwmWrite(13,61)
pulse=61

server_socket = BluetoothSocket(RFCOMM)
server_socket.bind(("",PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
uuid="1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
advertise_service( server_socket, "SampleServer",service_id = uuid,service_classes = [ uuid,SERIAL_PORT_CLASS ],profiles = [SERIAL_PORT_PROFILE ])
client_socket, address = server_socket.accept()

while True:
  data = client_socket.recv(1)
  client_socket.send(data)
  print'Received data:', data
  if (str(data) == 'a'):
      setpoint = 61
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
      pulse = setpoint 
  if (str(data) == 'b'):
      setpoint = 98
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
      pulse = setpoint
  if (str(data) == 'c'):
      setpoint = 140
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
      pulse = setpoint
  if (str(data) == 'd'):
      setpoint = 166
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
      pulse = setpoint
  if (str(data) == 'e'):
      setpoint = 195
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
      pulse = setpoint
  
  if(str(data)== '0'):
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(16, 0)
    GPIO.output(15, 0)
    GPIO.output(11, 0)
  if(str(data)== '1'):
   # GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(16, 0)
    GPIO.output(15, 0)
    GPIO.output(11, 0)
    GPIO.output(22, 1)
  if(str(data)== '2'):
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(16, 0)
    GPIO.output(15, 0)
    GPIO.output(11, 0)
    GPIO.output(18, 1)
  if(str(data)== '3'):
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    #GPIO.output(16, 0)
    GPIO.output(15, 0)
    GPIO.output(11, 0)
    GPIO.output(16, 1)
  if(str(data)== '4'):
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(16, 0)
    #GPIO.output(15, 0)
    GPIO.output(11, 0)
    GPIO.output(15, 1)
  if(str(data)== '5'):
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(16, 0)
    GPIO.output(15, 0)
    #GPIO.output(11, 0)
    GPIO.output(11, 1)
  if(str(data)== 'p'):
    call('sudo poweroff',shell = True)
client_socket.close()
server_socket.close()
