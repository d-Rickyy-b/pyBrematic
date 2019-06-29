# -*- coding: utf-8 -*-
import unittest

from pyBrematic.devices import AutoPairDevice
from pyBrematic.devices.intertechno import ITL500
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway
from pyBrematic.exceptions import GatewayNotSupportedException
from unittest.mock import Mock


class TestITL500(unittest.TestCase):
    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

        seed = 8712387
        self.dev = ITL500(123, seed)

    def test_invalid_gateway(self):
        with self.assertRaises(GatewayNotSupportedException):
            fake_gateway = Mock()
            self.dev.get_signal(fake_gateway, AutoPairDevice.ACTION_UP)

    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            fake_action = Mock()
            self.dev.get_signal(self.itgw, fake_action)

    def test_up_intertechno(self):
        up_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(up_signal_ITGW, self.dev.get_signal(self.itgw, AutoPairDevice.ACTION_UP))

    def test_up_brennenstuhl(self):
        up_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(up_signal_BSGW, self.dev.get_signal(self.bsgw, AutoPairDevice.ACTION_UP))

    def test_down_intertechno(self):
        down_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(down_signal_ITGW, self.dev.get_signal(self.itgw, AutoPairDevice.ACTION_DOWN))

    def test_down_brennenstuhl(self):
        down_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(down_signal_BSGW, self.dev.get_signal(self.bsgw, AutoPairDevice.ACTION_DOWN))

    def test_other_seed_intertechno(self):
        seed2 = 89090823173454879234
        dev_new = ITL500(1234, seed2)

        up_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        down_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(up_signal_ITGW, dev_new.get_signal(self.itgw, AutoPairDevice.ACTION_UP))
        self.assertEqual(down_signal_ITGW, dev_new.get_signal(self.itgw, AutoPairDevice.ACTION_DOWN))

    def test_other_seed_brennenstuhl(self):
        seed2 = 89090823173454879234
        dev_new = ITL500(1234, seed2)

        up_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,126"
        down_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(up_signal_BSGW, dev_new.get_signal(self.bsgw, AutoPairDevice.ACTION_UP))
        self.assertEqual(down_signal_BSGW, dev_new.get_signal(self.bsgw, AutoPairDevice.ACTION_DOWN))

    def test_unpair_all_intertechno(self):
        unpair_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15,3,3,3,3,3," + "3,112,0"
        self.assertEqual(unpair_signal_ITGW, self.dev.get_signal(self.itgw, AutoPairDevice.ACTION_UNPAIR_ALL))

    def test_unpair_all_brennenstuhl(self):
        unpair_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15,3,3,3,3,3," + "3,126"
        self.assertEqual(unpair_signal_BSGW, self.dev.get_signal(self.bsgw, AutoPairDevice.ACTION_UNPAIR_ALL))
