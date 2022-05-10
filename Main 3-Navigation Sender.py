# terminal_bot_controller_wireless.py

from microbit import *
import radio

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

print("\nSpeeds are -100 to 100\n")

while True:
    vL = int(input("Enter left speed: "))
    vR = int(input("Enter right speed: "))
    ms = int(input("Enter ms to run: "))

    dictionary = {  }
    dictionary['vL'] = vL
    dictionary['vR'] = vR
    dictionary['ms'] = ms

    packet = str(dictionary)
    
    print("Send: ", packet)
    radio.send(packet)
    
    print()