import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	p = GPIO.PWM(LedPin, 2000)
	p.start(100)

def loop():
	while True:
		for i in range(0, 101):
			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		time.sleep(1)
		for i in range(0, 101)[::-1]:	# reverse
			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		time.sleep(1)

def destroy():
	p.stop()
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
