# -*- coding: utf-8 -*-

import unittest

from pyBrematic.devices import Action
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

        on_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,32,0"
        off_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,32,0"

        self.assertEqual(device.get_signal(self.itgw, Action.ON), on_signal_ITGW)
        self.assertEqual(device.get_signal(self.itgw, Action.OFF), off_signal_ITGW)

        on_signal_BSGW = "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,14;"
        off_signal_BSGW = "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,14;"

        self.assertEqual(device.get_signal(self.bsgw, Action.ON), on_signal_BSGW)
        self.assertEqual(device.get_signal(self.bsgw, Action.OFF), off_signal_BSGW)
