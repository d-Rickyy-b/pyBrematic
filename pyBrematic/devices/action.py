# -*- coding: utf-8 -*-
"""Action class to identify the executed action"""
from enum import Enum


class Action(Enum):
    # Actions for remote power outlets / switching on and off
    OFF = 0
    ON = 1

    # Actions for roller blinds / moving up and down
    UP = 2
    DOWN = 3

    # Action for pairing/unpairing devices
    PAIR = UP
    UNPAIR = DOWN
    UNPAIR_ALL = 4
