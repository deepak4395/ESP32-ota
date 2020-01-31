# DHT Sensor
import dht
from time import sleep
from machine import Pin
d = dht.DHT22(Pin(33))
def dht22():
    print("dht22")
    d.measure()
    t=d.temperature() 
    h=d.humidity() 
    return t, h;

while(1):
    print(dht22())
    sleep(1)
    