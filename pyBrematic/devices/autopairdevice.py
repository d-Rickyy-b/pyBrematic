# -*- coding: utf-8 -*-
"""Device class representing a remote-controllable receiver"""
from pyBrematic.utils import Storage


class AutoPairDevice(object):
    ACTION_OFF = 0
    ACTION_ON = 1
    ACTION_UP = 2
    ACTION_DOWN = 3
    ACTION_PAIR = 4
    ACTION_UNPAIR = 5
    ACTION_UNPAIR_ALL = 6

    def __init__(self, device_id, seed):
        self.device_id = device_id
        storage = Storage()
        self.seed = seed or storage.get_seed(device_id)

    def get_signal(self, gateway, action):
        """Returns a signal which triggers a device to execute the intended action"""
        raise NotImplementedError("Subclasses must implement this method!")

