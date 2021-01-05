# -*- coding: utf-8 -*-

from pyBrematic.devices.device import Device
from .tools import calc_systemcode, calc_unitcode


class IntertechnoDevice(Device):
    """Base class for Intertechno devices using system/unit code"""

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        super().get_signal(action)

    @staticmethod
    def calc_systemcode(master):
        return calc_systemcode(master)

    @staticmethod
    def calc_unitcode(slave):
        return calc_unitcode(slave)
