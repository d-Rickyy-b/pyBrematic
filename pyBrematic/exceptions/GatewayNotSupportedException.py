# -*- coding: utf-8 -*-


class GatewayNotSupportedException(Exception):
    def __init__(self, message="Specified gateway is not supported!"):
        super().__init__(message)
