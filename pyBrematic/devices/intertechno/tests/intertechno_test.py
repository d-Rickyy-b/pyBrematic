# -*- coding: utf-8 -*-

import unittest

from pyBrematic.action import Action
from pyBrematic.devices.intertechno import PAR1500, CMR1000, ITR3500


class TestIntertechno(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_PAR1500(self):
        """Test to check the functionality of the PAR1500 class"""
        dev = PAR1500("1000", "1111")

        on_signal = "4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4"
        off_signal = "4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_CMR1000(self):
        """Test to check the functionality of the CMR1000 class"""
        dev = CMR1000("0000", "0010")  # binary representation of A5

        on_signal = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4"
        off_signal = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

        on_signal_2 = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4"
        off_signal_2 = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12"

        system_code = dev.calc_systemcode("A")
        unit_code = dev.calc_unitcode(5)
        dev2 = CMR1000(system_code, unit_code)

        self.assertEqual(on_signal_2, dev.get_signal(Action.ON))
        self.assertEqual(on_signal_2, dev2.get_signal(Action.ON))
        self.assertEqual(off_signal_2, dev.get_signal(Action.OFF))
        self.assertEqual(off_signal_2, dev2.get_signal(Action.OFF))

    def test_CMR1000_generation(self):
        system_code = CMR1000.calc_systemcode("P")
        unit_code = CMR1000.calc_unitcode(16)
        dev = CMR1000(system_code, unit_code)
        on_signal = "4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4"
        off_signal = "4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12"
        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_invalid_action(self):
        """Test to check if invalid actions raise an exception"""
        device = CMR1000("0000", "0010")

        with self.assertRaises(ValueError):
            _ = device.get_signal("WrongAction!")

    def test_valid_action(self):
        """Test to check if valid actions are set up correctly"""
        device = CMR1000("0000", "0010")

        self.assertIsNotNone(device.supported_actions.get(Action.ON))
        self.assertIsNotNone(device.supported_actions.get(Action.OFF))

        self.assertEqual(device.on, device.supported_actions.get(Action.ON))
        self.assertEqual(device.off, device.supported_actions.get(Action.OFF))

    def test_ITR3500(self):
        """Test to check the functionality of the ITR3500 class"""
        dev = ITR3500("0000", "0010")  # binary representation of A5

        on_signal = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4"
        off_signal = "4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12"

        self.assertEqual(on_signal, dev.get_signal(Action.ON))
        self.assertEqual(off_signal, dev.get_signal(Action.OFF))

    def test_calc_unitcode(self):
        with self.assertRaises(expected_exception=ValueError):
            CMR1000.calc_unitcode(-1)

        with self.assertRaises(expected_exception=ValueError):
            CMR1000.calc_unitcode(17)

    def test_calc_systemcode(self):
        with self.assertRaises(expected_exception=ValueError):
            CMR1000.calc_systemcode("Z")

        with self.assertRaises(expected_exception=ValueError):
            CMR1000.calc_systemcode("-")


if __name__ == "__main__":
    unittest.main()
