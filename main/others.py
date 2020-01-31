# Connect to router, 
ssid = "V30"
Pass = "sakshi1996"
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, Pass)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

#do_connect()

import os
print(os.listdir())
file = open("test.txt", "w")
writtenCharacters = file.write("Hello World!!!")
 
print(writtenCharacters)
 
file.close()
 
#print(os.size("test.txt"))

fileToRead = open("test.txt")
content = fileToRead.read()
print(content)
 
fileToRead.close()

# import _thread
# import time
#  
# def testThread(description, count):
#     print(description)
#     print(count)
#     while True:
#         print("Hello from thread")
#         time.sleep(2)
#      
# #_thread.start_new_thread(testThread, ("Hi",5))
