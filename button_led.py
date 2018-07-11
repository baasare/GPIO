from gpiozero import LED, Button
from signal import pause
from time import sleep
from subprocess import call

led = LED(17)
button = Button(2)



def blink():
	if button.when_pressed:
		while True:
			led.on()
			sleep(1)
			led.off()
			sleep(1)	
	elif button.when_pressed:
			led.off()


button.when_pressed = blink()

