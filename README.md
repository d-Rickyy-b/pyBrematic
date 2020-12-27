[![Build Status](https://travis-ci.com/d-Rickyy-b/pyBrematic.svg?branch=master)](https://travis-ci.com/d-Rickyy-b/pyBrematic)
[![PyPI version](https://badge.fury.io/py/pyBrematic.svg)](https://pypi.org/project/pyBrematic)
[![Coverage Status](https://coveralls.io/repos/github/d-Rickyy-b/pyBrematic/badge.svg?branch=master)](https://coveralls.io/github/d-Rickyy-b/pyBrematic?branch=master)

# pyBrematic
This project offers a home for controlling your remote power outlets (and potentially other stuff) with the Python programming language. With the help of the community we might get other devices working aswell.

### Installation
You can simply install the module via [pip](https://de.wikipedia.org/wiki/Pip_(Python)) like this:

`pip install pyBrematic`

If you have multiple versions of Python installed, make sure to use the Python 3 package manager:

`pip3 install pyBrematic`

And if you are having issues with installing the package, try to use the `--user` switch, to [install it to your home directory](https://stackoverflow.com/questions/42988977/what-is-the-purpose-pip-install-user).

### Example usage
To check out how to use the module, go to the [example file](https://github.com/d-Rickyy-b/pyBrematic/blob/master/pyBrematic/example/example.py) where I wrote a little example script, to show how to use the module.

### Important notice
Since all data packets are sent to the gateways via [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol), it cannot be guaranteed, that all requests will be transmitted to the gateway. For critical purposes you cannot rely on sending the signal once.
