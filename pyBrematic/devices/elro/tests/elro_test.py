# -*- coding: utf-8 -*-

import unittest

from pyBrematic.action import Action
from pyBrematic.devices.elro import AB440SA
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class TestElro(unittest.TestCase):

    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

    def tearDown(self):
        pass

    def test_AB440SA(self):
        system_code = "10000"
        unit_code = "00100"
        device = AB440SA(system_code=system_code, unit_code=unit_code)

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, device.get_signal(Action.ON))
        self.assertEqual(off_signal, device.get_signal(Action.OFF))

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(on_signal, device.get_signal(Action.ON))
        self.assertEqual(off_signal, device.get_signal(Action.OFF))

    def test_invalid_action(self):
        """Test to check if invalid actions raise an exception"""
        system_code = "10000"
        unit_code = "00100"
        device = AB440SA(system_code=system_code, unit_code=unit_code)

        with self.assertRaises(ValueError):
            _ = device.get_signal("WrongAction!")

    def test_valid_action(self):
        """Test to check if valid actions are set up correctly"""
        system_code = "10000"
        unit_code = "00100"
        device = AB440SA(system_code=system_code, unit_code=unit_code)

        self.assertIsNotNone(device.supported_actions.get(Action.ON))
        self.assertIsNotNone(device.supported_actions.get(Action.OFF))

        self.assertEqual(device.on, device.supported_actions.get(Action.ON))
        self.assertEqual(device.off, device.supported_actions.get(Action.OFF))


if __name__ == "__main__":
    unittest.main()
