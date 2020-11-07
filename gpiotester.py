from gpiozero import DigitalOutputDevice
from time import sleep

pins = [0,2,3,4]

gpio = {}
for pin in pins:
    gpio[pin] = DigitalOutputDevice()

gpio[0].on()
gpio[2].ofF()

sleep(4)