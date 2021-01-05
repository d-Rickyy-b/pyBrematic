# -*- coding: utf-8 -*-

import unittest

from pyBrematic.action import Action
from pyBrematic.devices.brennenstuhl import RCR1000N, RCS1000N
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class TestBrennenstuhl(unittest.TestCase):

    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

    def tearDown(self):
        pass

    def test_RCR1000N(self):
        """Test to check the functionality of the RCR1000N class"""
        dev = RCR1000N("10000", "00100")

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_RCR1000N_10000_00000(self):
        """Test to check the functionality of the RCR1000N class"""
        # Taken from https://github.com/Power-Switch/PowerSwitch_Android/blob/54400f74230bb78f87b19cc89c0f174e080a3fa7/Smartphone/src/androidTest/java/eu/power_switch/obj/device/brennenstuhl/RCS1000NComfort_Test.java#L97
        dev = RCR1000N("10000", "00000")

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_RCR1000N_10000_10000(self):
        """Test to check the functionality of the RCR1000N class"""
        dev = RCR1000N("10000", "10000")

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_RCS1000N(self):
        """Test to check the functionality of the RCS1000N class"""
        dev = RCS1000N("10000", "00100")

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_invalid_action(self):
        """Test to check if invalid actions raise an exception"""
        system_code = "10000"
        unit_code = "00100"
        device = RCS1000N(system_code=system_code, unit_code=unit_code)

        with self.assertRaises(ValueError):
            _ = device.get_signal("WrongAction!")

    def test_valid_action(self):
        """Test to check if valid actions are set up correctly"""
        system_code = "10000"
        unit_code = "00100"
        device = RCS1000N(system_code=system_code, unit_code=unit_code)

        self.assertIsNotNone(device.supported_actions.get(Action.ON))
        self.assertIsNotNone(device.supported_actions.get(Action.OFF))

        self.assertEqual(device.on, device.supported_actions.get(Action.ON))
        self.assertEqual(device.off, device.supported_actions.get(Action.OFF))

if __name__ == "__main__":
    unittest.main()
