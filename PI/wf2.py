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
