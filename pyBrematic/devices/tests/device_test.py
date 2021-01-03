# -*- coding: utf-8 -*-

import unittest

from pyBrematic.action import Action
from pyBrematic.devices import Device


class TestDevice(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Device(self):
        """Test to make sure that call to method raises an exception"""
        dev = Device("10000", "00100")
        with self.assertRaises(NotImplementedError):
            dev.get_signal(Action.ON)
