import time
from machine import Pin
red_led = Pin(15,mode=Pin.OUT)
#red_led.value(0)
btn =Pin(14,mode=Pin.PULL_DOWN)
is_press = False
led_status = False

def btn_detect(btn1):
    global is_press,led_status
    if btn1.value():
        time.sleep_ms(50)
        if btn.value():
            is_press=True
    elif is_press:
        time.sleep_ms(50)
        if btn1.value()==False:
            print("release")
            led_status = not led_status
            red_led.value(led_status)
            is_press = False
            
                
while True:
    if btn.value():
        is_press=True
        #red_led.value(1)
        #print("按下")
        #time.sleep_ms(500)
    elif is_press:
        time.sleep_ms(300)
        print("release")
        is_press=False
        
       # red_led.value(0)
