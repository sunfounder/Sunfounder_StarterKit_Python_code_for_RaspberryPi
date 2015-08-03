import RPi.GPIO as GPIO
import time

BEEP = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BEEP, GPIO.OUT)

def loop():
	while True:
		GPIO.output(BEEP, not(GPIO.input(BEEP)))
		time.sleep(1)

def destroy():
	GPIO.output(BEEP, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
