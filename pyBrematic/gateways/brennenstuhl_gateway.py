# -*- coding: utf-8 -*-
import socket

from pyBrematic.gateways.gateway import Gateway


class BrennenstuhlGateway(Gateway):
    """Gateway class for the Brennenstuhl Brematic Gateway GWY 433 1294100"""

    def __init__(self, ip, port=49880):
        super().__init__(ip, port)
        # Each UDP package sent to the gateway must contain certain parameters set in a header and a tail.
        # These are format strings used to insert those parameters.
        # For the Brematic GWY 433 the parameters look like that:
        # head: "TXP:0,0,<repeat>,<pause>,<tune>,<baud>"
        # tail: "<txversion>,<speed>;"
        self.head_format = "TXP:0,0,{0},{1},{2},{3}"
        self.tail_format = "{0},{1};"

    def build_udp_payload(self, device, action):
        head = self.get_head(device.repeat, device.pause_BS, device.tune, device.baud)
        tail = self.get_tail(device.txversion, device.speed_BS)
        payload = device.get_signal(self, action)

        return ",".join([head, payload, tail])

    def send_request(self, device, action):
        """Sends the UDP request to the gateway"""
        payload = self.build_udp_payload(device, action)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload.encode(), (self._ip, self._port))
        s.close()
