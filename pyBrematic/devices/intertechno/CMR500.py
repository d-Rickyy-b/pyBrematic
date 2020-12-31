# -*- coding: utf-8 -*-
# Reference: https://github.com/Power-Switch/PowerSwitch_Android/blob/master/Smartphone/src/main/java/eu/power_switch/obj/receiver/device/intertechno/CMR500.java
# Since this is a dimmer, I am not sure if this code also supports dimming or only switchig.

from .CMR1000 import CMR1000


class CMR500(CMR1000):
    """Device class for the Intertechno CMR-500 switch"""

    def __init__(self, system_code, unit_code):
        super().__init__(system_code, unit_code)
