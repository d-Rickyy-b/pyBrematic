# -*- coding: utf-8 -*-
"""Action class to identify the executed action"""
from enum import Enum


class Action(Enum):
    OFF = 0
    ON = 1
    UP = 2
    DOWN = 3
    PAIR = 4
    UNPAIR = 5
    UNPAIR_ALL = 6
