# -*- coding: utf-8 -*-

from pyBrematic.devices import Device, Action
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class AB440SA(Device):
    """Device class for the ELRO AB440SA  remote outlet"""
    lo = "1,"
    hi = "3,"
    seq_low = lo + hi + lo + hi
    seq_high = lo + hi + hi + lo

    sRepeat = 10
    sPauseBS = 5600
    sPauseIT = 11200
    sTune = 350
    sBaudBS = 25
    sBaudIT = 26
    sSpeedBS = 14
    sSpeedIT = 32
    txversion = 1

    headITGW = "0,0,{},{},{},{},0,".format(sRepeat, sPauseIT, sTune, sBaudIT)
    tailITGW = "{},{},0".format(txversion, sSpeedIT)

    headBSGW = "TXP:0,0,{},{},{},{},".format(sRepeat, sPauseBS, sTune, sBaudBS)
    tailBSGW = "{},{};".format(txversion, sSpeedBS)

    on = seq_low + seq_high
    off = seq_high + seq_low

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    @staticmethod
    def encode(code, seq_low, seq_high):
        """Method for encoding the system_code or unit_code from binary to a gateway-readable format"""
        encoded_msg = ""
        for bit in code:
            if bit == "0":
                encoded_msg += seq_high
            elif bit == "1":
                encoded_msg += seq_low
            else:
                raise ValueError("Invalid value in system_code or unit_code!")
        return encoded_msg

    def get_signal(self, gateway, action):
        """Returns a signal which triggers a device to execute the intended action"""
        system_msg = self.encode(self.system_code, self.seq_low, self.seq_high)
        unit_msg = self.encode(self.unit_code, self.seq_low, self.seq_high)

        if isinstance(gateway, BrennenstuhlGateway):
            head = self.headBSGW
            tail = self.tailBSGW
        elif isinstance(gateway, IntertechnoGateway):
            head = self.headITGW
            tail = self.tailITGW

        # Build the payload of the UDP package depending on the action.
        if action == Action.ON:
            data = head + system_msg + unit_msg + self.on + tail
        elif action == Action.OFF:
            data = head + system_msg + unit_msg + self.off + tail
        else:
            raise ValueError("Value of 'action' isn't valid!")

        return data
