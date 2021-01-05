# -*- coding: utf-8 -*-

from .brennenstuhl_gateway import BrennenstuhlGateway


class ConnAirGateway(BrennenstuhlGateway):
    def __init__(self, ip, port=49880):
        super().__init__(ip, port)
