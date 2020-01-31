from main.ota_updater import OTAUpdater
ssid = "M 57"
password = "8376918157"
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
def download_and_install_update_if_available():    
    ota_updater.download_and_install_update_if_available(ssid,password)

def start():
    print("in Code")

def boot():
    download_and_install_update_if_available()
    start()

boot()
ota_updater.check_for_update_to_install_during_next_reboot()
