# -*- coding: utf-8 -*-
"""Device class representing a remote-controlled receiver"""


class Device(object):
    ACTION_OFF = 0
    ACTION_ON = 1

    def __init__(self, system_code, unit_code):
        self.system_code = system_code
        self.unit_code = unit_code

    def get_signal(self, gateway, action):
        """Returns a signal which triggers a device to execute the intended action"""
        raise NotImplementedError("Subclasses must implement this method!")
