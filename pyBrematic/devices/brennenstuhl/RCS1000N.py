# -*- coding: utf-8 -*-

from pyBrematic.devices.device import Device


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
    sPause = 5600
    sTune = 350
    sBaud = 25
    sSpeed = 16
    txversion = 1

    head = "TXP:0,0,{},{},{},{},".format(sRepeat, sPause, sTune, sBaud)
    tail = "{},1,{};".format(txversion, sSpeed)

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 1 | bit_high: 1 -> 3
    lo = "1,"
    hi = "3,"

    seq_low = hi + hi + lo + lo
    seq_high = hi + lo + hi + lo

    # These sequences are the commands for switching a device on or off
    # On:  01011 -> encoded: 13133
    # Off: 10010 -> encoded: 31131
    on = lo + hi + lo + hi + hi
    off = hi + lo + lo + hi + lo

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    # Method for encoding the system_code or unit_code from binary to a gateway-readable format
    @staticmethod
    def encode(code, seq_low, seq_high):
        encoded_msg = ""
        for bit in code:
            if bit == "0":
                encoded_msg += seq_low
            elif bit == "1":
                encoded_msg += seq_high
            else:
                raise ValueError("Invalid value in system_code or unit_code!")
        return encoded_msg

    def get_signal(self, gateway, action):
        # Encoding the system_code and unit_code
        system_msg = self.encode(self.system_code, self.seq_low, self.seq_high)
        unit_msg = self.encode(self.unit_code, self.seq_low, self.seq_high)

        # Build the payload of the UDP package depending on the action.
        if action == self.ACTION_ON:
            data = self.head + self.lo + system_msg + unit_msg + self.hi + self.on + self.tail
        elif action == self.ACTION_OFF:
            data = self.head + self.lo + system_msg + unit_msg + self.hi + self.off + self.tail
        else:
            raise ValueError("Value of 'action' isn't valid!")

        return data
