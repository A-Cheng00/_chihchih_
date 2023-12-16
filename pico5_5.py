import network
import time

ssid=""
password=""

wlan= network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()
wlan.connect(ssid,password)

#

