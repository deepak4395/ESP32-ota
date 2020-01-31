from main.ota_updater import OTAUpdater
import machine
from time import sleep

ssid = "M 57"
password = "8376918157"

def Project():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
    ota_updater = OTAUpdater('https://github.com/deepak4395/ESP32-ota')
    ota_updater.download_and_install_update_if_available(ssid,password)
    if (ota_updater.check_for_update_to_install_during_next_reboot()):
        machine.reset()
    while 1 :        
        print("Hello")
        sleep(1)
