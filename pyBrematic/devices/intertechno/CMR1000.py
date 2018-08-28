# -*- coding: utf-8 -*-
from pyBrematic.devices.device import Device
from pyBrematic.exceptions import GatewayNotSupportedException
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class CMR1000(Device):
    """Device class for the Intertechno CMR-1000 remote outlet"""
    sRepeat = 6
    sPause = 11125
    sTune = 89
    sBaudBS = 25
    sBaudIT = 26
    sSpeedBS = 140
    sSpeedIT = 125
    txversion = 1

    headBSGW = "TXP:0,0,{},{},{},{},".format(sRepeat, sPause, sTune, sBaudBS)
    tailBSGW = "{},{};".format(txversion, sSpeedBS)

    headITGW = "0,0,{},{},{},{},0,".format(sRepeat, sPause, sTune, sBaudIT)
    tailITGW = "{},{},0".format(txversion, sSpeedIT)

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 1 | bit_high: 1 -> 3
    lo = "4,"
    hi = "12,"

    seq_low = lo + hi + lo + hi
    seq_fl = lo + hi + hi + lo

    on = seq_fl + seq_fl
    off = seq_fl + seq_low
    additional = seq_low + seq_fl

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
        """Returns a signal which triggers a device to execute the intended action"""
        # Encoding the system_code and unit_code
        system_msg = self.encode(self.system_code, self.seq_low, self.seq_fl)
        unit_msg = self.encode(self.unit_code, self.seq_low, self.seq_fl)

        if isinstance(gateway, BrennenstuhlGateway):
            head = self.headBSGW
            tail = self.tailBSGW
        elif isinstance(gateway, IntertechnoGateway):
            head = self.headITGW
            tail = self.tailITGW
        else:
            raise GatewayNotSupportedException

        # Build the payload of the UDP package depending on the action.
        if action == self.ACTION_ON:
            data = head + system_msg + unit_msg + self.additional + self.on + tail
        elif action == self.ACTION_OFF:
            data = head + system_msg + unit_msg + self.additional + self.off + tail
        else:
            raise ValueError("Value of 'action' isn't valid!")

        return data
