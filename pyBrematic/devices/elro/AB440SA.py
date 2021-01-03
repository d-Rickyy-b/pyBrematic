# -*- coding: utf-8 -*-

from pyBrematic.action import Action
from pyBrematic.devices import Device


class AB440SA(Device):
    """Device class for the ELRO AB440SA remote outlet"""
    repeat = 10
    tune = 350
    txversion = 1

    pause_BS = 5600
    pause_IT = 11200

    baud_BS = 25
    baud_IT = 26

    speed_BS = 14
    speed_IT = 32

    lo = "1"
    hi = "3"
    seq_low = [lo, hi, lo, hi]
    seq_high = [lo, hi, hi, lo]

    on = seq_low + seq_high
    off = seq_high + seq_low
    supported_actions = {Action.ON: on, Action.OFF: off}

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        system_msg = self.encode(self.system_code, self.seq_low, self.seq_high)
        unit_msg = self.encode(self.unit_code, self.seq_low, self.seq_high)

        action_signal = self.supported_actions.get(action)

        # Build the payload of the UDP package depending on the action.
        if not action_signal:
            raise ValueError("Value of 'action' isn't valid!")

        data = system_msg + unit_msg + action_signal

        return self.join_list(data)
