from gpiozero import DigitalOutputDevice

pin = 0

gpio = DigitalOutputDevice(pin)

gpio.on()

DigitalOutputDevice(2).off()