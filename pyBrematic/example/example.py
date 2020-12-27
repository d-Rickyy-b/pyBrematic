# -*- coding: utf-8 -*-
"""This is an example usage file for the pyBrematic module"""

from pyBrematic.devices.brennenstuhl import RCS1000N
from pyBrematic.gateways import BrennenstuhlGateway

# Set your system and unit codes
system_code = "11110"  # Switches 1-4 are in the 'up' position, 5 is 'down'
unit_code = "10000"  # Switch A is in the 'up' position, B-E are 'down'

# Create a new device with the specified codes
desk_lamp = RCS1000N(system_code, unit_code)

# Create a new gateway located at the specified IP
gw = BrennenstuhlGateway("192.168.178.9")

# Send the request and pass it the device and the action (on/off)
gw.send_request(desk_lamp, desk_lamp.ACTION_ON)
gw.send_request(desk_lamp, desk_lamp.ACTION_OFF)
