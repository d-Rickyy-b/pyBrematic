# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock

from pyBrematic import Action
from pyBrematic.gateways import ConnAirGateway


class TestConnAirGateway(unittest.TestCase):

    def setUp(self):
        self.ip = "192.168.1.100"
        self.port = "1234"
        self.gw = ConnAirGateway(self.ip, self.port)

    def test_build_udp_payload(self):
        """Test if building the UDP payload for the ConnAir GW works correctly"""
        device = Mock()
        device.repeat = 2345
        device.pause_BS = 917
        device.tune = 557
        device.baud = 91919
        device.txversion = 1
        device.speed_BS = 234

        function = Mock()
        function.return_value = "A,SIGNAL-A,B,B,A-SIGNAL,C"
        device.get_signal = function

        payload = self.gw.build_udp_payload(device, Action.ON)
        self.assertEqual("TXP:0,0,2345,917,557,91919,A,SIGNAL-A,B,B,A-SIGNAL,C,1,234;", payload)

    def test_get_head(self):
        """Test if formatting the 'head' string works with random data"""
        self.gw.head_format = "1{0}----{1}++++{2}ASDF{3}#24/"
        head = self.gw.get_head(777, "ASDF1", 313, "-A-")
        self.assertEqual("1777----ASDF1++++313ASDF-A-#24/", head)

    def test_get_tail(self):
        """Test if formatting the 'tail' string works with random data"""
        self.gw.tail_format = "1{0}---++---{1}++ASDF#24/"
        tail = self.gw.get_tail("//-ASDF1", 313)
        self.assertEqual("1//-ASDF1---++---313++ASDF#24/", tail)

    def test_missing_head_format(self):
        """Test if missing 'head' format is handled correctly"""
        self.gw.head_format = None
        with self.assertRaises(ValueError):
            _ = self.gw.get_head("1", "2", "3", "4")

    def test_invalid_tail_format(self):
        """Test if missing 'tail' format is handled correctly"""
        self.gw.tail_format = None
        with self.assertRaises(ValueError):
            _ = self.gw.get_tail("1", "2")


if __name__ == '__main__':
    unittest.main()
