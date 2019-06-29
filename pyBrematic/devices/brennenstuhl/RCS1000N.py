# -*- coding: utf-8 -*-

from pyBrematic.devices import Device, Action
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


# SYSTEM-CODE | unit code
#  1 2 3 4 5  | A B C D E
#  1 0 0 0 0  | 1 0 0 0 0 -> 1 A
# A '1' in this representation means that the switch in your remote control
# is in the 'up' position.

class RCS1000N(Device):
    """Device class for the Brennenstuhl RCS-1000N remote outlet"""
    # Syntax of the request for the RCS1000N is:
    # |-------Header--------|                                                      |-tail-|
    # TXP:0,0,10,5600,350,25,<bit_low>,<enc_system_code>,<enc_unit_code>,<bit_high>,1,1,16;
    # Check http://luckow.org/archive/brennenstuhl.html (german) for more info about this.
    # Parameters for the requests. Only change if you have good reasons for it
    sRepeat = 10
    sPauseBS = 5600
    sPauseIT = 11200
    sTune = 350
    sBaudBS = 25
    sBaudIT = 26
    sSpeedBS = 16
    sSpeedIT = 32
    txversion = 1

    headBSGW = "TXP:0,0,{},{},{},{},".format(sRepeat, sPauseBS, sTune, sBaudBS)
    tailBSGW = "{},{};".format(txversion, sSpeedBS)

    headITGW = "0,0,{},{},{},{},0,".format(sRepeat, sPauseIT, sTune, sBaudIT)
    tailITGW = "{},{},0".format(txversion, sSpeedIT)

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 1 | bit_high: 1 -> 3
    lo = "1,"
    hi = "3,"

    seq_low = lo + hi + lo + hi
    seq_high = lo + hi + hi + lo

    # These sequences are the commands for switching a device on or off
    # On:  01011 -> encoded: 13133
    # Off: 10010 -> encoded: 31131
    on = seq_low + seq_high
    off = seq_high + seq_low

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    # Method for encoding the system_code or unit_code from binary to a gateway-readable format
    @staticmethod
    def encode(code, seq_low, seq_high):
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
        # Encoding the system_code and unit_code
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
