import RPi.GPIO as GPIO
import time

LedPin = 11
TiltPin = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
	while True:
		if GPIO.input(TiltPin) == 0:
			GPIO.output(LedPin, 0)
		else:
			GPIO.output(LedPin, 1)

def destroy():
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
