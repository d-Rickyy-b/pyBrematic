# Device class representing a Brennenstuhl remote socket-outlet
# SYSTEM-CODE | unit code
#  1 2 3 4 5  | A B C D E
#  1 0 0 0 0  | 1 0 0 0 0 -> 1 A
# A '1' in this representation means that the switch in your remote control
# is in the 'up' position.


class Device(object):
    ACTION_OFF = 0
    ACTION_ON = 1

    def __init__(self, system_code, unit_code):
        self._system_code = system_code
        self._unit_code = unit_code

    @property
    def system_code(self):
        return self._system_code

    @system_code.setter
    def system_code(self, s_code):
        self._system_code = s_code

    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, u_code):
        self._unit_code = u_code
