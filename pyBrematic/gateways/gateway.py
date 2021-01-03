# -*- coding: utf-8 -*-
"""Gateway class to inherit from, for 433 MHz gateways"""


# Idea and help taken from this websites
# http://luckow.org/archive/brennenstuhl.html
# https://www.symcon.de/forum/threads/27143


class Gateway(object):

    # '49880' is the standard port for the Brennenstuhl GWY 433
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self.head_format = None
        self.tail_format = None

    def get_head(self, repeat, pause, tune, baud):
        if not self.head_format:
            raise ValueError("No head_format found for gateway")
        return self.head_format.format(repeat, pause, tune, baud)

    def get_tail(self, txversion, speed):
        if not self.tail_format:
            raise ValueError("No tail_format found for gateway")
        return self.tail_format.format(txversion, speed)

    def send_request(self, device, action):
        raise NotImplementedError("Subclasses must implement this method!")
