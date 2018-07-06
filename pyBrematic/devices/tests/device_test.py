# -*- coding: utf-8 -*-

import unittest

from pyBrematic.devices.device import Device
from pyBrematic.gateways.brennenstuhl_gateway import BrennenstuhlGateway


class Devices(unittest.TestCase):

    def setUp(self):
        self.gw = BrennenstuhlGateway("192.168.178.2")

    def tearDown(self):
        pass

    def test_a(self):
        dev = Device("10000", "00100")
        with self.assertRaises(NotImplementedError):
            dev.get_signal(self.gw, Device.ACTION_ON)
