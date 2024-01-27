from machine import Timer,Pin,ADC
import time
from tools import connect,reconnect

url = 'https://blynk.cloud/external/api/batch/update?token=sk3fTHgDtabGCPLQa0R13fB7KXRBMKH6&v0=1&v1=2'

def fun10(t:Timer | None = None):
    print("10秒了")
    led.toggle()
    
def fun10ms(t):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')
    
connect()
led=Pin(15,Pin.OUT)
light = ADC(Pin(28))
vr = ADC(Pin(27))
#time10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
time10ms = Timer(period=2000, mode=Timer.PERIODIC, callback=fun10ms)
fun10()