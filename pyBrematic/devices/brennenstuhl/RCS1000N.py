# -*- coding: utf-8 -*-

from pyBrematic.action import Action
from pyBrematic.devices import Device


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
    repeat = 10
    tune = 350
    txversion = 1

    pause_BS = 5600
    pause_IT = 11200

    baud_BS = 25
    baud_IT = 26

    speed_BS = 16
    speed_IT = 32

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 1 | bit_high: 1 -> 3
    lo = "1"
    hi = "3"

    seq_low = [lo, hi, lo, hi]
    seq_high = [lo, hi, hi, lo]

    # These sequences are the commands for switching a device on or off
    # On:  01011 -> encoded: 13133
    # Off: 10010 -> encoded: 31131
    on = seq_low + seq_high
    off = seq_high + seq_low
    supported_actions = {Action.ON: on, Action.OFF: off}

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        # Encoding the system_code and unit_code
        system_msg = self.encode(self.system_code, self.seq_low, self.seq_high)
        unit_msg = self.encode(self.unit_code, self.seq_low, self.seq_high)

        action_signal = self.supported_actions.get(action)

        # Build the payload of the UDP package depending on the action.
        if not action_signal:
            raise ValueError("Value of 'action' isn't valid!")

        data = system_msg + unit_msg + action_signal

        return self.join_list(data)
