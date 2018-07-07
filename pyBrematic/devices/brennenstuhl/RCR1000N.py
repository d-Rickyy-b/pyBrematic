# -*- coding: utf-8 -*-

# Since the RCR 1000N works exactly the same as the RCS 1000N, there is no
# further logic implemented in this class
from pyBrematic.devices.brennenstuhl.RCS1000N import RCS1000N


class RCR1000N(RCS1000N):
    """Device class for the RCR 1000N remote outlet"""

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)
