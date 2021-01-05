# -*- coding: utf-8 -*-

import unittest

from pyBrematic.action import Action
from pyBrematic.devices import AutoPairDevice
from pyBrematic.gateways import BrennenstuhlGateway


class TestAutoPairDevice(unittest.TestCase):

    def setUp(self):
        self.gw = BrennenstuhlGateway("192.168.178.2")

    def tearDown(self):
        pass

    def test_Device(self):
        """Test to make sure that call to method raises an exception"""
        dev = AutoPairDevice("10000", "00100")
        with self.assertRaises(NotImplementedError):
            dev.get_signal(Action.ON)
