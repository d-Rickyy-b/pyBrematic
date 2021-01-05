# -*- coding: utf-8 -*-
import re


def calc_system_and_unit_code(code):
    """Calculates the (binary) system and unit code from a given string such as "A5", "B11", "F8"

    :param code: The alphanumeric code such as "D7"
    :return: Tuple of string representation of binary values (system, unit) - e.g.: ("0100", "1000")
    """
    pattern = r"([A-P])(\d+)"
    match = re.match(pattern, code)
    if not match:
        raise ValueError("Code must start with a letter A-P and end in a number 1-16!")

    system_ascii = match.group(1)
    unit_ascii = match.group(2)

    system_bin = calc_systemcode(system_ascii)
    unit_bin = calc_unitcode(int(unit_ascii))
    return system_bin, unit_bin


def calc_systemcode(master):
    """Calculates the (binary) system code from a given string such as "A", "B", "F"

    :param master: The system channel letter such as "D"
    :return: String representation of binary value - e.g.: "0100"
    """
    if master == "":
        raise ValueError("Value must not be empty!")

    master = master.upper()

    # Check if master is in range [A-P]
    number = ord(master) - 65
    if number not in range(0, 16 + 1):
        raise ValueError("Master value '{}' is not ranged between [1, 16]".format(master))

    systemcode = "{0:04b}".format(number)
    return systemcode[::-1]


def calc_unitcode(slave):
    """Calculates the (binary) system code from a given channel number such as 3, 8, 15

    :param slave: The unit channel number such as 11
    :return: String representation of binary value - e.g.: "0100"
    """
    if slave not in range(1, 16 + 1):
        raise ValueError("Slave value '{}' is not ranged between [1, 16]".format(slave))

    unitcode = "{0:04b}".format(slave - 1)
    return unitcode[::-1]
