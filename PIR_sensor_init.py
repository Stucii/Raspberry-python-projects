import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) ##pulldown is an internal resistor
##if you dont have he pulldown == the default is zero or low, no movement reads low, movement read high

while True:
    time.sleep(0.10)
    print(GPIO.input(PIR_PIN))
GPIO.input(PIR_PIN)


GPIO.cleanup()