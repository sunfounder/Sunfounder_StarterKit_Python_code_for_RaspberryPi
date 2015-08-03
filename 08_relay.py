import RPi.GPIO as GPIO
import time

RelayPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(RelayPin, GPIO.OUT)

def loop():
	while True:
		GPIO.output(RelayPin, 0)
		time.sleep(0.5)
		GPIO.output(RelayPin, 1)
		time.sleep(0.5)

def destroy():
	GPIO.output(RelayPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
