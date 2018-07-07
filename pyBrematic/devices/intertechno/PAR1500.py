# -*- coding: utf-8 -*-

from pyBrematic.devices.intertechno.CMR1000 import CMR1000


# The PAR-1500 uses the same technology as the CMR-1000
class PAR1500(CMR1000):
    """Device class for the Intertechno PAR-1000 remote outlet"""

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)
