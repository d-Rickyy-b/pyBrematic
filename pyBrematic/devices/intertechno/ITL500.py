# -*- coding: utf-8 -*-
from pyBrematic.devices import AutoPairDevice, Action
from pyBrematic.exceptions import GatewayNotSupportedException
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway
from pyBrematic.utils import Rand


class ITL500(AutoPairDevice):
    """Device class for the Intertechno ITL-500 sun blind switch"""
    headBSGW = "TXP:0,0,5,10976,98,66,3,29,"
    tailBSGW = "3,126"

    headITGW = "0,0,5,10976,98,67,0,3,29,"
    tailITGW = "3,112,0"

    lo = "3,"
    hi = "15,"

    seq_low = lo + lo + lo + hi
    seq_fl = lo + hi + lo + lo

    on = seq_low + seq_low + seq_fl
    off = seq_low + seq_low + seq_low
    additional = seq_low + seq_low

    def __init__(self, device_id, seed=None):
        super().__init__(device_id, seed)

    def get_signal(self, gateway, action):
        """Returns a signal which triggers a device to execute the intended action"""
        # Encoding the system_code and unit_code
        prng = Rand(self.seed)
        signal = ""
        data = ""

        if isinstance(gateway, BrennenstuhlGateway):
            head = self.headBSGW
            tail = self.tailBSGW
        elif isinstance(gateway, IntertechnoGateway):
            head = self.headITGW
            tail = self.tailITGW
        else:
            raise GatewayNotSupportedException

        # Build the payload of the UDP package depending on the action.
        if action == Action.UNPAIR_ALL:
            for i in range(24):
                signal += self.lo

            signal += self.lo + self.lo + self.hi + self.lo
            signal += self.lo + self.lo + self.lo + self.lo

            data = head + signal + tail

        elif action == Action.UP or action == Action.PAIR:
            # When the receiver is in pairing mode, the first ON signal sent to the device will be stored by it.
            # Using a prng and a stored seed to generate the same number sequence in each request
            signal += self.hi

            for i in range(24):
                if prng.next_bool():
                    signal += self.hi
                else:
                    signal += self.lo

            signal += self.on

            for i in range(2):
                if prng.next_bool():
                    signal += self.hi
                else:
                    signal += self.lo

            signal += self.additional

            data = head + signal + tail
        elif action == Action.DOWN or action == Action.UNPAIR:
            signal += self.hi

            for i in range(24):
                if prng.next_bool():
                    signal += self.hi
                else:
                    signal += self.lo

            signal += self.off

            for i in range(2):
                if prng.next_bool():
                    signal += self.hi
                else:
                    signal += self.lo

            signal += self.additional

            data = head + signal + tail
        else:
            raise ValueError("Value of 'action' isn't valid!")

        return data
