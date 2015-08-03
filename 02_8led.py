import RPi.GPIO as GPIO
import time

led = [11, 12, 13, 15, 16, 18, 22, 7]

def led_on(n):
	GPIO.output(n, 0)

def led_off(n):
	GPIO.output(n, 1)

def setup():
	GPIO.setmode(GPIO.BOARD)
	for i in led:
		GPIO.setup(i, GPIO.OUT)

def loop():
	while True:
		for i in range(0, 8):
			led_on(led[i])
			time.sleep(0.1)
			led_off(led[i])

		for i in range(0, 8):
			led_on(led[7-i])
			time.sleep(0.1)
			led_off(led[7-i])

def destroy():
	for i in led:
		GPIO.output(i, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
