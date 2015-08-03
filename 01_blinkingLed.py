import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)

def loop():
	while True:
		GPIO.output(LedPin, 0)
		time.sleep(0.5)
		GPIO.output(LedPin, 1)
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
