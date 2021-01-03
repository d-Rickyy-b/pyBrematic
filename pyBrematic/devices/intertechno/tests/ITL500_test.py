# -*- coding: utf-8 -*-
import unittest

from pyBrematic import Action
from pyBrematic.devices.intertechno import ITL500
from unittest.mock import Mock


class TestITL500(unittest.TestCase):
    def setUp(self):
        seed = 8712387
        self.dev = ITL500(123, seed)

    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            fake_action = Mock()
            self.dev.get_signal(fake_action)

    def test_up_signal(self):
        up_signal = "3,29,15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15"
        self.assertEqual(up_signal, self.dev.get_signal(Action.UP))

    def test_down_signal(self):
        down_signal = "3,29,15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15"
        self.assertEqual(down_signal, self.dev.get_signal(Action.DOWN))

    def test_other_seed(self):
        seed2 = 89090823173454879234
        dev_new = ITL500(1234, seed2)

        up_signal = "3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15"
        down_signal = "3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15"
        self.assertEqual(up_signal, dev_new.get_signal(Action.UP))
        self.assertEqual(down_signal, dev_new.get_signal(Action.DOWN))

    def test_unpair_all(self):
        unpair_signal = "3,29," + "3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,15,3,3,3,3,3"
        self.assertEqual(unpair_signal, self.dev.get_signal(Action.UNPAIR_ALL))
