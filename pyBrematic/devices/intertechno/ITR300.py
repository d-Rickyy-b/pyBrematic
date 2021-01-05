# -*- coding: utf-8 -*-
from pyBrematic.devices.intertechno import CMR1000


class ITR300(CMR1000):
    """Device class for the Intertechno ITR-300 remote outlet"""

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)
