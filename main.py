import time
import wiringpi
from time import sleep
from bluetooth import *
import bluetooth
import RPi.GPIO as GPIO
from subprocess import call
import adafruit_vl6180x
import board
import busio
import subprocess
import smbus
import select

def performAction(data):
  if (data.decode() == 'a'):
      setpoint = 144
      wiringpi.pwmWrite(13,setpoint)
      time.sleep(0.5);
  elif (data.decode() == 'b'):
      setpoint = 60
      wiringpi.pwmWrite(13,setpoint)
      time.sleep(0.5);
  elif (data.decode() == 'c'):
      setpoint = 100
      wiringpi.pwmWrite(13,setpoint)
      time.sleep(0.5);
  elif (data.decode() == 'd'):
      setpoint = 193
      wiringpi.pwmWrite(13,setpoint)
      time.sleep(0.5);
  elif (data.decode() == 'e'):
      setpoint =236
      wiringpi.pwmWrite(13,setpoint)
      time.sleep(0.5);
  elif(data.decode()== '0'):
    GPIO.output(nwhite, 0)
    GPIO.output(n395nm, 0)
    GPIO.output(n415nm, 0)
    GPIO.output(22, 0)
    GPIO.output(n365nm, 0)
  elif(data.decode()== '1'):
    GPIO.output(nwhite, 0)
    GPIO.output(n395nm, 0)
    GPIO.output(n415nm, 0)
    GPIO.output(22, 0)
    GPIO.output(n365nm, 0)
  elif(data.decode()== '2'):
    GPIO.output(nwhite, 0)
    GPIO.output(n395nm, 0)
    GPIO.output(n415nm, 0)
    GPIO.output(n365nm, 1)
    GPIO.output(22, 0)
  elif(data.decode()== '3'):
    GPIO.output(nwhite, 0)
    GPIO.output(n395nm, 1)
    GPIO.output(n415nm, 0)
    GPIO.output(n365nm, 0)
    GPIO.output(22, 0)
  elif(data.decode()== '4'):
    GPIO.output(nwhite, 0)
    GPIO.output(n395nm, 0)
    GPIO.output(n415nm, 1)
    GPIO.output(n365nm, 0)
    GPIO.output(22, 0)
  elif(data.decode()== '5'):
    GPIO.output(nwhite, 1)
    GPIO.output(n395nm, 0)
    GPIO.output(n415nm, 0)
    GPIO.output(n365nm, 0)
    GPIO.output(22, 0)
  elif(data.decode()=='g'):
    GPIO.output(18,GPIO.HIGH)
  elif(data.decode()== 'p'):
    call('sudo poweroff',shell = True)
  elif(data.decode()== 'm'):
   try:
    bus.read_byte(0x29) 
    sensor=adafruit_vl6180x.VL6180X(i2c)
    range_mm=sensor.range
    data=bytes([int(range_mm)])
   except:
    print("Error234234")
  return data
sensor = 0
nwhite = 25
n395nm = 24
n415nm = 23
n365nm = 17
subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(nwhite, GPIO.OUT)
GPIO.setup(n395nm, GPIO.OUT)
GPIO.setup(n415nm, GPIO.OUT)
GPIO.setup(n365nm, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(nwhite, 0)
GPIO.setup(n395nm, 0)
GPIO.setup(n415nm, 0)
GPIO.setup(n365nm, 0)
GPIO.setup(22, 0)
GPIO.setup(18, 0)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period = 0.01
wiringpi.pwmWrite(13,144)
pulse=144
i2c = busio.I2C(board.SCL, board.SDA)
bus = smbus.SMBus(1)
server_socket = BluetoothSocket(RFCOMM)
server_socket.bind(("",PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
uuid="1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
advertise_service( server_socket, "SampleServer",service_id = uuid,service_classes = [ uuid,SERIAL_PORT_CLASS ],profiles = [SERIAL_PORT_PROFILE ])
client_socket, address = server_socket.accept()
while True:
  try:
    data = client_socket.recv(1)
    client_socket.send(performAction(data))
    print(data)
    print("-------------------------------------------------------")
  except bluetooth.btcommon.BluetoothError:
    print("Logic Fail___Restarting")
    client_socket.close()
    server_socket.close() 
    server_socket = BluetoothSocket(RFCOMM)
    server_socket.bind(("",PORT_ANY))
    server_socket.listen(1)
    port = server_socket.getsockname()[1]
    uuid="1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
    advertise_service( server_socket, "SampleServer",service_id = uuid,service_classes = [ uuid,SERIAL_PORT_CLASS ],profiles = [SERIAL_PORT_PROFILE ])
    client_socket, address = server_socket.accept()
    time.sleep(1)
client_socket.close()
server_socket.close()
