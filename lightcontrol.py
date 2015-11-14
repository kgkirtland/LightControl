#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Home Automation --- Remote-controlled Light Control
#
#

import sys
import os
from LightController import LightController
from RpiGpioInterface import RpiGpioInterface
from TimeWrapper import TimeWrapper

lightPinsList = [23, 24]

gpioInterface = RpiGpioInterface()
timeWrapper = TimeWrapper()
lightController = LightController(lightPinsList, gpioInterface, timeWrapper)

def Init():
    os.system('clear')

def ShowMenu():
    prompt = '>>:  '

    selection = None

    print
    print("===========================================================")
    print(" HOME AUTOMATION --- REMOTE-CONTROLLED LIGHT CONTROL")
    print("===========================================================")
    print

    print("1. Lights Off!")
    print("2. Lights On!")
    print("3. Light Show")
    print("4. Exit")

    while (selection != 4):
        try:
            print
            selection=int(raw_input(prompt))

            if (selection == 1): 
                print("Turning lights off...")
                lightController.LightsOff()
            elif (selection == 2):
                print("Turning lights on...") 
                lightController.LightsOn()
            elif (selection == 3):
                print("Running light show (Ctrl-C to quit)...") 
                try:
                    lightController.RunLightShow(10)
                except KeyboardInterrupt:
                    print
                    print("Exiting light show...")
            elif (selection == 4): Exit()
            else: print "Invalid selection. Please try again."
        except ValueError:
            print "Invalid selection."

def Exit():
    lightController.LightsOff()
    print("Exiting...")
    print
    lightController.Cleanup()
    sys.exit()

if __name__ == "__main__":
    Init()
    ShowMenu()
