# -*- coding: utf-8 -*-
"""Device class representing a remote-controlled receiver"""
from pyBrematic.action import Action


class Device(object):
    ACTION_OFF = Action.OFF
    ACTION_ON = Action.ON

    def __init__(self, system_code, unit_code):
        self.system_code = system_code
        self.unit_code = unit_code

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        raise NotImplementedError("Subclasses must implement this method!")

    @staticmethod
    def encode(code, seq_low, seq_high):
        """Method for encoding the system_code or unit_code from binary to a gateway-readable format"""
        encoded_msg = []
        for bit in code:
            if bit == "0":
                encoded_msg += seq_high
            elif bit == "1":
                encoded_msg += seq_low
            else:
                raise ValueError("Invalid value in system_code or unit_code!")
        return encoded_msg

    @staticmethod
    def join_list(lst, delimeter=","):
        """Join a list together with a certain delimeter

        :param lst: The list to join
        :param delimeter: The delimeter to use to join the list elements
        :return:
        """
        return delimeter.join(lst)
