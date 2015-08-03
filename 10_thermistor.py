#!/usr/bin/env python
import ADC0832 as ADC
import RPi.GPIO as GPIO
import time

def setup():
	ADC.setup()

def loop():
	while True:
		analogVal = ADC.getResult(0)
		print 'adcval:', analogVal
		time.sleep(0.4)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
