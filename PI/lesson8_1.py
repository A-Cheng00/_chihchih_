from machine import Timer,Pin,ADC
import time
from tools import connect,reconnect



def fun10(t:Timer | None = None):
    light_value= light.read_u16()
    vr_value = vr_value.read_u16()
    url = f'https://blynk.cloud/external/api/batch/update?token=sk3fTHgDtabGCPLQa0R13fB7KXRBMKH6&v0={light_value}&v1={vr_value}'
    try:
        led.value(1)
        response = requests.get(url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("傳送失敗")
    led.value(1)        
    
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