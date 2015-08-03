#!/usr/bin/env python
import ADC0832 as ADC
import RPi.GPIO as GPIO
import time

LED = 15

def setup():
	global p
	ADC.setup()
	GPIO.setup(LED, GPIO.OUT)
	p = GPIO.PWM(LED, 2000)
	p.start(100)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def loop():
	while True:
		analogVal = ADC.getResult(0)
		print analogVal
		#p.ChangeDutyCycle(analogVal-150)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		p.stop()
		GPIO.cleanup()
