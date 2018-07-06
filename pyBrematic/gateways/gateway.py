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

    def send_request(self, device, action):
        raise NotImplementedError("Subclasses must implement this method!")
