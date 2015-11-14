#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Home Automation --- Raspberry Pi GPIO Light Controller
#
#

import random
from TimeWrapper import TimeWrapper

class LightController(object):
    def __init__(self, lightPinsList, gpioInterface, timeWrapper):
        self._lightPinsList = lightPinsList
        self._gpioInterface = gpioInterface
        self._timeWrapper = timeWrapper

        for lightPin in self._lightPinsList:
            self._gpioInterface.SetOutPin(lightPin)

    def LightsOff(self):
        """
        Sends off signal to each light pin
        """
        for lightPin in self._lightPinsList:
            self._gpioInterface.SetPinHigh(lightPin)

    def LightsOn(self):
        """
        Sends on signal to each light pin
        """
        for lightPin in self._lightPinsList:
            self._gpioInterface.SetPinLow(lightPin)

    def RunLightShow(self, cycleLimit):
        """
        Runs light show
        """
        timeDelayDivider = 3
        x = 1

        while True: 
            if x > cycleLimit : x = 1 #reset counter once it hits the cycle limit

            self.LightShowSequence(x, timeDelayDivider)

            x = x + 1

    def LightShowSequence(self, x, timeDelayDivider):
        """
        Execute light show sequence
        """
        selectedLight = self.GetRandomLightPin()
        self.BlinkLight(selectedLight, x / timeDelayDivider)
        selectedLight = self.GetRandomLightPin()
        self._gpioInterface.SetPinHigh(selectedLight) if x % 2 == 0 else self._gpioInterface.SetPinLow(selectedLight)
        self._timeWrapper.sleep(.5 * x)

    def BlinkLight(self, selectedLight, timeDelay):
        """
        Blinks light according to time delay
        """
        self._gpioInterface.SetPinLow(selectedLight)
        self._timeWrapper.sleep(timeDelay)
        self._gpioInterface.SetPinHigh(selectedLight)
    
    def GetRandomLightPin(self):
        """
        Returns random light pin from list
        """
        selectedLight = random.choice(self._lightPinsList)
        return selectedLight

    def Cleanup(self):
        """
        Performs cleanup to light pins
        """
        self._gpioInterface.Cleanup()
