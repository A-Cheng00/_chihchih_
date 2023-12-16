#a=0
#for a in range(10)
#print("a")

import time
from machine import Pin

led=Pin("LED",Pin.OUT)

while True:
    led.on()
    time.sleep(10)
    led.off()
    time.sleep(1)
