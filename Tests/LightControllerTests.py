#
# Kenny Kirtland
# @2015
#
# Light Controller Tests
#
#

import unittest
from unittest import TestCase
from mock import patch, MagicMock
from LightController import LightController
from RpiGpioInterface import RpiGpioInterface
from TimeWrapper import TimeWrapper

@patch('RpiGpioInterface.RpiGpioInterface')
@patch('TimeWrapper.TimeWrapper')
class LightControllerTest(TestCase):
    _testLightPinsList = [23, 24]

    def test_Init_VerifyNotNone(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        self.assertIsNotNone(lightsController)

    def test_LightsOn_Verify_SetPinLow_CalledForEachListElement(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        lightsController.LightsOn()
        self.assertEqual(mockedRpi.SetPinLow.call_count, len(self._testLightPinsList))

    def test_LightShowSequence_Verify_SetPinHigh_Called(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        x = 5
        timeDelayDivider = 7
        lightsController.LightShowSequence(x, timeDelayDivider)
        self.assertTrue(mockedRpi.SetPinHigh.called)

    def test_LightShowSequence_Verify_Sleep_Called(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        x = 5
        timeDelayDivider = 7
        lightsController.LightShowSequence(x, timeDelayDivider)
        self.assertTrue(mockedTimeWrapper.sleep.called)
       
    def test_LightsOff_Verify_SetPinHigh_CalledForEachListElement(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        lightsController.LightsOff()
        self.assertEqual(mockedRpi.SetPinHigh.call_count, len(self._testLightPinsList))

    def test_BlinkLight_Verify_SetPinLow_And_SetPinHigh_Called_Once(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        selectedLight = 9
        timeDelay = 1
        lightsController.BlinkLight(selectedLight, timeDelay)
        mockedRpi.SetPinLow.assert_called_once_with(selectedLight)
        mockedRpi.SetPinHigh.assert_called_once_with(selectedLight)

    def test_BlinkLight_Verify_Sleep_Called_Once_With_Delay(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        selectedLight = 8
        timeDelay = 3
        lightsController.BlinkLight(selectedLight, timeDelay)
        mockedTimeWrapper.sleep.assert_called_once_with(timeDelay)
    
    def test_Cleanup_Verify_RpiGpioCleanup_Called_Once(self, mockedRpi, mockedTimeWrapper):
        lightsController = LightController(self._testLightPinsList, mockedRpi, mockedTimeWrapper)
        lightsController.Cleanup()
        mockedRpi.Cleanup.assert_called_once_with()
                
if __name__ == '__main__':
    unittest.main()
