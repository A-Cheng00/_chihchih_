from machine import Timer,Pin

def fun10(t:Timer):
    print("10秒了")

time10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
