# -*- coding: utf-8 -*-
from pyBrematic.action import Action
from pyBrematic.devices import AutoPairDevice
from pyBrematic.utils import Rand


class ITL500(AutoPairDevice):
    """Device class for the Intertechno ITL-500 sun blind switch"""
    repeat = 5
    tune = 98
    txversion = 3

    pause_BS = 10976
    pause_IT = 10976

    baud_BS = 66
    baud_IT = 67

    speed_IT = 112
    speed_BS = 126

    lo = "3"
    hi = "15"

    seq_low = [lo, lo, lo, hi]
    seq_fl = [lo, hi, lo, lo]

    on = seq_low + seq_low + seq_fl
    off = seq_low + seq_low + seq_low
    additional = seq_low + seq_low

    def __init__(self, device_id, seed=None):
        super().__init__(device_id, seed)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        # Encoding the system_code and unit_code
        prng = Rand(self.seed)
        signal = ["3", "29"]

        # Build the payload of the UDP package depending on the action.
        if action == Action.UNPAIR_ALL:
            for i in range(24):
                signal.append(self.lo)

            signal += [self.lo, self.lo, self.hi, self.lo]
            signal += [self.lo, self.lo, self.lo, self.lo]

        elif action == Action.UP or action == Action.PAIR:
            # When the receiver is in pairing mode, the first ON signal sent to the device will be stored by it.
            # Using a prng and a stored seed to generate the same number sequence in each request
            signal.append(self.hi)

            for i in range(24):
                signal.append(self.hi if prng.next_bool() else self.lo)

            signal += self.on

            for i in range(2):
                signal.append(self.hi if prng.next_bool() else self.lo)

            signal += self.additional

        elif action == Action.DOWN or action == Action.UNPAIR:
            signal.append(self.hi)

            for i in range(24):
                signal.append(self.hi if prng.next_bool() else self.lo)

            signal += self.off

            for i in range(2):
                signal.append(self.hi if prng.next_bool() else self.lo)

            signal += self.additional

        else:
            raise ValueError("Value of 'action' isn't valid!")

        return self.join_list(signal)
