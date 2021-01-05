# -*- coding: utf-8 -*-
"""This is an example usage file for the pyBrematic module"""

from pyBrematic import Action
from pyBrematic.devices.brennenstuhl import RCS1000N
from pyBrematic.devices.intertechno import ITR3500, calc_system_and_unit_code
from pyBrematic.gateways import BrennenstuhlGateway

# Set your system and unit codes
system_code = "11110"  # DIPs 1-4 are in the 'up' position, 5 is 'down'
unit_code = "10000"  # DIP A is in the 'up' position, B-E are 'down'

# Create a new device with the specified codes
desk_lamp = RCS1000N(system_code, unit_code)

# For Intertechno devices you can also use the following methods to get the code
# via master/slave (letter/number) notation. Allowed values are "A-P" and "1-16".
led_system_code, led_unit_code = calc_system_and_unit_code("A3")
led_strip = ITR3500(led_system_code, led_unit_code)

# Create a new gateway located at the specified IP
gw = BrennenstuhlGateway("192.168.178.9")

# Send the request and pass it the device and the action (on/off)
gw.send_request(desk_lamp, Action.ON)
gw.send_request(desk_lamp, Action.OFF)
