# pyBrematic

[![Build Status](https://travis-ci.com/d-Rickyy-b/pyBrematic.svg?branch=master)](https://travis-ci.com/d-Rickyy-b/pyBrematic)
[![PyPI version](https://badge.fury.io/py/pyBrematic.svg)](https://pypi.org/project/pyBrematic)
[![Coverage Status](https://coveralls.io/repos/github/d-Rickyy-b/pyBrematic/badge.svg?branch=master)](https://coveralls.io/github/d-Rickyy-b/pyBrematic?branch=master)

The topic "smart home" or "home automation" in particular has become increasingly popular throughout the last few years. While many manufacturers are relying
on cloud infrastructure, there are some that produce local-only devices, using the 433 MHz ISM band.

The python module "pyBrematic" enables you to control and automate your 433 MHz remote power outlets (and other switches/dimmers) with the Python programming
language. All you need for this is a supported 433 MHz network gateway, such as the `Intertechno ITGW-433`, the `Brematic GWY 433` (or `CONNAIR 433`, which is
basically the same as the Brematic one).

With the help of the community we might get other devices working as well.

### Installation

This module is available on pypi and hence can be downloaded via pip like this:

`pip install pyBrematic`

And if you are having issues with installing the package, try to use the `--user` switch,
to [install it to your home directory](https://stackoverflow.com/questions/42988977/what-is-the-purpose-pip-install-user).  
PyBrematic has no external dependencies. Only Python versions >= 3.5 are supported.

### Example usage

To check out how to use the module, go to the [example file](https://github.com/d-Rickyy-b/pyBrematic/blob/master/pyBrematic/example/example.py). There you'll
find an example configuration of how to use the module.

```python
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
```

### Important notice

Since all data packets are sent to the gateways via [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol), it cannot be guaranteed, that all requests
will be received by the gateway. For critical purposes you cannot rely on sending the signal once.
