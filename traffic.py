from gpiozero import LED, Button
from time import sleep
from signal import pause,signal

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
button = Button(2)

def start_traffic():
	while True:
	    led2.on()
	    sleep(3)
	    led2.off()
	    if button.is_pressed:
			sleep(3)
			continue
		
		led1.on()
	    sleep(10)
	    led1.off()


	    led3.on()
	    sleep(10)
	    led3.off()
	    
	    
	    
button.when_pressed = start_traffic
pause()
