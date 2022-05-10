# terminal_controlled_bot_wireless

from cyberbot import *
import radio

radio.on()
radio.config(channel=16,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Receive: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(16).servo_speed(vL)
        bot(17).servo_speed(-vR)
        sleep(ms)
        bot(16).servo_speed(None)
        bot(17).servo_speed(None)