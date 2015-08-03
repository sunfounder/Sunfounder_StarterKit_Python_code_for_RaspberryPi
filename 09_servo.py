import RPi.GPIO as GPIO
import time

ServoPin = 11

def setup():
	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ServoPin, GPIO.OUT)
	p = GPIO.PWM(ServoPin, 3000)
	p.start(100)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def turnServo(degree):
	freq = map(degree, 0, 180, 0, 100)
	p.ChangeDutyCycle(freq)

def loop():
	while True:
		for i in range(0, 180):
			turnServo(i)
			time.sleep(0.1)
		time.sleep(1)
		for i in range(0, 180)[::-1]:	# reverse
			turnServo(i)
			time.sleep(0.1)
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
