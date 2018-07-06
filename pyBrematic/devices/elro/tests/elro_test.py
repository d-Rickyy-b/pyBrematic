# -*- coding: utf-8 -*-

import unittest

from pyBrematic.gateways.brennenstuhl_gateway import BrennenstuhlGateway
from pyBrematic.devices.elro.AB440SA import AB440SA
import pyBrematic.devices.device


class Elro(unittest.TestCase):

    def setUp(self):
        self.gw = BrennenstuhlGateway("192.168.178.2")

    def tearDown(self):
        pass

    def test_AB440SA(self):
        system_code = "10000"
        unit_code = "00100"
        device = AB440SA(system_code=system_code, unit_code=unit_code)

        on_signal = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,32,0"
        off_signal = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,32,0"

        self.assertEqual(device.get_signal(self.gw, device.ACTION_ON), on_signal)
        self.assertEqual(device.get_signal(self.gw, device.ACTION_OFF), off_signal)
