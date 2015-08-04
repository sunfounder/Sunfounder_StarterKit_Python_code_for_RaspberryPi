#!/usr/bin/env python
import ADC0832 as ADC
import RPi.GPIO as GPIO
import time

Beep = 15

def setup():
	ADC.setup()
	GPIO.setup(Beep, GPIO.OUT)

def beep():
	GPIO.output(Beep, 0)
	time.sleep(0.5)
	GPIO.output(Beep, 1)
	time.sleep(0.5)

def loop():
	while True:
		analogVal = ADC.getResult(0)
		print 'adcval:', analogVal
		if analogVal > 200:
			beep()
		else:
			time.sleep(0.5)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
