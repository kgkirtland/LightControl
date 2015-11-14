#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Home Automation --- Raspberry Pi GPIO Interface
#
#

import RPi.GPIO as gpio

class RpiGpioInterface(object):
    def __init__(self):
        gpio.setmode(gpio.BCM)

    def SetOutPin(self, pinNumber):
        gpio.setup(pinNumber, gpio.OUT)

    def SetPinHigh(self, pinNumber):
        gpio.output(pinNumber, gpio.HIGH)

    def SetPinLow(self, pinNumber):
        gpio.output(pinNumber, gpio.LOW)

    def Cleanup(self):
        gpio.cleanup()

