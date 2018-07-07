# -*- coding: utf-8 -*-

import unittest

from pyBrematic.devices.brennenstuhl.RCR1000N import RCR1000N
from pyBrematic.devices.brennenstuhl.RCS1000N import RCS1000N
from pyBrematic.devices.device import Device
from pyBrematic.gateways.brennenstuhl_gateway import BrennenstuhlGateway
from pyBrematic.gateways.intertechno_gateway import IntertechnoGateway


class Devices(unittest.TestCase):

    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

    def tearDown(self):
        pass

    def test_RCR1000N(self):
        dev = RCR1000N("10000", "00100")

        on_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,32,0"
        off_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,32,0"

        self.assertEqual(on_signal_ITGW, dev.get_signal(self.itgw, Device.ACTION_ON))
        self.assertEqual(off_signal_ITGW, dev.get_signal(self.itgw, Device.ACTION_OFF))

        on_signal_BSGW =  "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,16;"
        off_signal_BSGW = "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,16;"

        self.assertEqual(on_signal_BSGW, dev.get_signal(self.bsgw, Device.ACTION_ON))
        self.assertEqual(off_signal_BSGW, dev.get_signal(self.bsgw, Device.ACTION_OFF))

    def test_RCS1000N(self):
        dev = RCS1000N("10000", "00100")

        on_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,32,0"
        off_signal_ITGW = "0,0,10,11200,350,26,0,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,32,0"

        on_signal_BSGW =  "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,16;"
        off_signal_BSGW = "TXP:0,0,10,5600,350,25,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,3,3,1,1,3,3,1,1,3,3,1,1,3,1,3,1,16;"

        self.assertEqual(on_signal_BSGW, dev.get_signal(self.bsgw, Device.ACTION_ON))
        self.assertEqual(off_signal_BSGW, dev.get_signal(self.bsgw, Device.ACTION_OFF))
