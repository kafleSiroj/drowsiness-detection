import serial
import time

# Replace 'COM3' with the actual port of your Arduino

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for connection to establish

def motor_on():
    if arduino:
        arduino.write('1'.encode())  # Add newline for proper parsing

def motor_off():
    if arduino:
        arduino.write('0'.encode())
