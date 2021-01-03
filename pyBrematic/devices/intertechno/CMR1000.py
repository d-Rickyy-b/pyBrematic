# -*- coding: utf-8 -*-
from pyBrematic.devices.intertechno import IntertechnoDevice
from pyBrematic.action import Action


class CMR1000(IntertechnoDevice):
    """Device class for the Intertechno CMR-1000 remote outlet"""
    repeat = 6
    tune = 89
    txversion = 1

    pause_BS = 11125
    pause_IT = 11125

    baud_BS = 25
    baud_IT = 26

    speed_BS = 140
    speed_IT = 125

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 4 | bit_high: 1 -> 12
    lo = "4"
    hi = "12"

    seq_low = [lo, hi, lo, hi]
    seq_fl = [lo, hi, hi, lo]

    on = seq_fl + seq_fl
    off = seq_fl + seq_low
    additional = seq_low + seq_fl
    supported_actions = {Action.ON: on, Action.OFF: off}

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        # Encoding the system_code and unit_code
        system_msg = self.encode(self.system_code, self.seq_fl, self.seq_low)
        unit_msg = self.encode(self.unit_code, self.seq_fl, self.seq_low)

        action_signal = self.supported_actions.get(action)

        # Build the payload of the UDP package depending on the action.
        if not action_signal:
            raise ValueError("Value of 'action' isn't valid!")

        data = system_msg + unit_msg + self.additional + action_signal

        return self.join_list(data)
