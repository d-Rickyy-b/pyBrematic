# -*- coding: utf-8 -*-
import socket

from pyBrematic.gateways.gateway import Gateway


class IntertechnoGateway(Gateway):
    """Gateway class for the Intertechno Gateway ITGW-433"""

    def __init__(self, ip, port=49880):
        super().__init__(ip, port)
        # Each UDP package sent to the gateway must contain certain parameters set in a header and a tail.
        # These are format strings used to insert those parameters.
        # For the Intertechno GWY 433 the parameters look like that:
        # head: "0,0,<repeat>,<pause>,<tune>,<baud>"
        # tail: "<txversion>,<speed>"
        self.head_format = "0,0,{0},{1},{2},{3}"
        self.tail_format = "{0},{1}"

    def build_udp_payload(self, device, action):
        head = self.get_head(device.repeat, device.pause_IT, device.tune, device.baud)
        tail = self.get_tail(device.txversion, device.speed_IT)
        payload = device.get_signal(self, action)

        return ",".join([head, payload, tail])

    def send_request(self, device, action):
        """Sends the UDP request to the gateway"""
        payload = self.build_udp_payload(device, action)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload.encode(), (self._ip, self._port))
        s.close()
