import network
import time

def connect():
    nic=network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect('Pixel_7849','10102222')

    max_wait=10
    while max_wait>0:
        max_wait -=1
        status=nic.status()
        if status<0 or status >=3:
            break
        print("等待連線")
        time.sleep(1)
        
    #while not nic.isconnected() and nic.status() >=0:
     #   print("等待連線")
      #  time.sleep(1)
       
    if nic.status() !=3:
        raise RuntimeError("連線失敗")
    else:
        print("cannot find")
        print("connected")

    print(nic.ifconfig())
    
from machine import ADC,Timer
import time
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.

def alert():
    print('要爆炸了!')
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert()
        start = time.ticks_ms()#重新設定計時的時間
 
connect() 

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒
    
time1 = Timer()
time1.init(period=1000,callback=callback1)


