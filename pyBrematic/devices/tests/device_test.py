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

    def test_encode_error(self):
        dev = Device("10000", "00100")
        with self.assertRaises(ValueError):
            dev.encode("000123000", "A", "B")

    def test_encode(self):
        dev = Device("10000", "00100")
        encoded = dev.encode("000111", "A", "B")
        self.assertEqual(list, type(encoded))
        self.assertEqual(["B", "B", "B", "A", "A", "A"], encoded)


if __name__ == "__main__":
    unittest.main()
