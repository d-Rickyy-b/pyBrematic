# -*- coding: utf-8 -*-

import unittest

from pyBrematic.devices import Action
from pyBrematic.devices.intertechno import PAR1500, CMR1000, ITR3500
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class TestIntertechno(unittest.TestCase):

    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

    def tearDown(self):
        pass

    def test_PAR1500(self):
        """Test to check the functionality of the PAR1500 class"""
        dev = PAR1500("1000", "1111")

        on_signal_ITGW = "0,0,6,11125,89,26,0,4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,125,0"
        off_signal_ITGW = "0,0,6,11125,89,26,0,4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,125,0"

        self.assertEqual(on_signal_ITGW, dev.get_signal(self.itgw, Action.ON))
        self.assertEqual(off_signal_ITGW, dev.get_signal(self.itgw, Action.OFF))

        on_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,140;"
        off_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,12,4,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,4,12,12,4,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,140;"

        self.assertEqual(on_signal_BSGW, dev.get_signal(self.bsgw, Action.ON))
        self.assertEqual(off_signal_BSGW, dev.get_signal(self.bsgw, Action.OFF))

    def test_CMR1000(self):
        """Test to check the functionality of the CMR1000 class"""
        dev = CMR1000("0000", "0010")  # binary representation of A5

        on_signal_ITGW = "0,0,6,11125,89,26,0,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,125,0"
        off_signal_ITGW = "0,0,6,11125,89,26,0,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,125,0"

        self.assertEqual(on_signal_ITGW, dev.get_signal(self.itgw, Action.ON))
        self.assertEqual(off_signal_ITGW, dev.get_signal(self.itgw, Action.OFF))

        on_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,140;"
        off_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,140;"

        self.assertEqual(on_signal_BSGW, dev.get_signal(self.bsgw, Action.ON))
        self.assertEqual(off_signal_BSGW, dev.get_signal(self.bsgw, Action.OFF))

    def test_ITR3500(self):
        """Test to check the functionality of the ITR3500 class"""
        dev = ITR3500("0000", "0010")  # binary representation of A5

        on_signal_ITGW = "0,0,6,11125,89,26,0,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,125,0"
        off_signal_ITGW = "0,0,6,11125,89,26,0,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,125,0"

        self.assertEqual(on_signal_ITGW, dev.get_signal(self.itgw, Action.ON))
        self.assertEqual(off_signal_ITGW, dev.get_signal(self.itgw, Action.OFF))

        on_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,12,4,1,140;"
        off_signal_BSGW = "TXP:0,0,6,11125,89,25,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,4,12,12,4,4,12,4,12,4,12,4,12,4,12,12,4,4,12,12,4,4,12,4,12,1,140;"

        self.assertEqual(on_signal_BSGW, dev.get_signal(self.bsgw, Action.ON))
        self.assertEqual(off_signal_BSGW, dev.get_signal(self.bsgw, Action.OFF))
