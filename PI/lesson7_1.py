import time
from machine import Pin
red_led = Pin(15,mode=Pin.OUT)
#red_led.value(0)
btn =Pin(14,mode=Pin.PULL_DOWN)
is_press = False
led_status = False

while True:
    if btn.value():
        is_press=True
        #red_led.value(1)
        #print("按下")
        #time.sleep_ms(500)
    else:
        if is_press == True:
            print("release")
            is_press = False    
       # red_led.value(0)
    
    
