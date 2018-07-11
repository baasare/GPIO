from gpiozero import LED, Button
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
button = Button(2)

def start_traffic():
	while True:
	    led1.on()
	    sleep(5)
	    led1.off()

	    led2.on()
	    sleep(1)
	    led2.off()

	    led3.on()
	    sleep(5)
	    led3.off()

button.when_pressed = start_traffic
