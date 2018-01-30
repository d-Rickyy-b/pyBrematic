# This is an example usage file for the pyBrematic module

from pyBrematic.devices.device import Device
from pyBrematic.gateways.brennenstuhl_gateway import BrennenstuhlGateway

# Setting the standard action to "on"
action = Device.ACTION_ON

# Set your system and unit codes
system_code = "11110"
unit_code = "10000"

# Create a new device with the specified codes
device = Device(system_code, unit_code)

# Create a new gateway located at the specified IP
gw = BrennenstuhlGateway("192.168.178.1")

# Send the request and pass it the device and the action (on/off)
gw.send_request(device, action)
