# -*- coding: utf-8 -*-
"""This is an example usage file for the pyBrematic module"""

from pyBrematic.devices import Action
from pyBrematic.devices.brennenstuhl import RCS1000N
from pyBrematic.devices.intertechno import ITR3500
from pyBrematic.devices.intertechno import calc_unitcode, calc_systemcode
from pyBrematic.gateways import BrennenstuhlGateway

# Set your system and unit codes
system_code = "11110"  # Switches 1-4 are in the 'up' position, 5 is 'down'
unit_code = "10000"  # Switch A is in the 'up' position, B-E are 'down'

# Create a new device with the specified codes
desk_lamp = RCS1000N(system_code, unit_code)

# You can also use the following methods to get the code via master/slave (letter/number) notation
led_system_code = calc_systemcode("A")
led_unit_code = calc_unitcode(3)
led_strip = ITR3500(led_system_code, led_unit_code)

# Create a new gateway located at the specified IP
gw = BrennenstuhlGateway("192.168.178.9")

# Send the request and pass it the device and the action (on/off)
gw.send_request(desk_lamp, Action.ON)
gw.send_request(desk_lamp, Action.OFF)
