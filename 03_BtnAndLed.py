import RPi.GPIO as GPIO
import time

LedPin = 11
ButtonPin = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
	while True:
		GPIO.output(LedPin, 1)
		if GPIO.input(ButtonPin) == 0:
			GPIO.output(LedPin, 0)

def destroy():
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
