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

        self.assertEqual(device.get_signal(Action.ON), on_signal)
        self.assertEqual(device.get_signal(Action.OFF), off_signal)

        on_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1"
        off_signal = "1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3"

        self.assertEqual(device.get_signal(Action.ON), on_signal)
        self.assertEqual(device.get_signal(Action.OFF), off_signal)
