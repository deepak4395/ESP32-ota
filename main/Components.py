print('Code Started')
import machine
from machine import Pin, PWM, ADC
from time import sleep, sleep_us
import math

# Ms, Pir, Stepper Motor, RGB Led, In led

# Pins Used 14(Ms), 12(Pir), 33(DHT), 32, 19, 18, 4, 25(R), 26(G), 27(B), 22(SCL), 21(SDA), 2(inLed)

# Magnetic Switch
def interruptM(pin):
    print("Magnetic Switch Change");
m = Pin(14,Pin.IN, Pin.PULL_DOWN)
m.irq(trigger=3, handler=interruptM)

# Motion Sensor
def interruptPir(pin):
    print("Motion Detected");
p = Pin(12,Pin.IN, Pin.PULL_DOWN)
p.irq(trigger=Pin.IRQ_RISING, handler=interruptPir)

# Battery 
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
xmax = (4095*3.4)/3.6
xmin = ((4095*2.4)/3.6)
xs = 100
def battery():
    x = adc.read() - xmin
    xp = (x/(xmax-xmin))*100
    if xp < 0:
        xs = 0
    elif xp > 100:
        xs = 100
    elif xs-xp>5:
        xs=xp
    return int(xs)

# Stepper Motor
P = [Pin(23, Pin.OUT, value=0),Pin(19, Pin.OUT, value=0),Pin(18, Pin.OUT, value=0),Pin(4, Pin.OUT, value=0)]
t=10000
Steps=15
def closeLock():
    print("Close")
    for j in range(0,Steps):
        for i in range(0,4):
            P[3-i].value(1)
            sleep_us(t)
            P[3-i].value(0)
            sleep_us(t)
def openLock():
    print("open")
    for j in range(0,Steps):
        for i in range(0,4):
            P[i].value(1)
            sleep_us(t)
            P[i].value(0)
            sleep_us(t)
# RGB
pwm1 = PWM(Pin(25), freq=5000)
pwm2 = PWM(Pin(26), freq=5000)
pwm3 = PWM(Pin(27), freq=5000)
def rgb(duty_cycle1, duty_cycle2, duty_cycle3):
    print("Rgb")
    pwm1.duty(duty_cycle1)
    pwm2.duty(duty_cycle2)
    pwm3.duty(duty_cycle3)

#Inbuilt led brightness control
pwm0 = PWM(Pin(2), freq=5000)
def inLed(duty_cycle):
    print("inLed")
    pwm0.duty(duty_cycle)
    
while(1):    
    print("Battery(%)", battery())
    openLock()
    rgb(255,255,255)
    inLed(0)
    #dht22() #need testing
    sleep(10)
    closeLock()

print("Code Ended")