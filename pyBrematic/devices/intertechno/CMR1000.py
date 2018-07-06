# -*- coding: utf-8 -*-

from pyBrematic.devices.device import Device


class CMR1000(Device):
    """Device class for the Intertechno CMR-1000 remote outlet"""
    sRepeat = 6
    sPause = 11125
    sTune = 89
    sBaud = 25
    sSpeed_conn_air = 16
    sSpeed_ITGW = 125
    txversion = 1

    head_conn_air = "TXP:0,0,{},{},{},{},".format(sRepeat, sPause, sTune, sBaud)
    head_ITGW = "0,0,{},{},{},{},0,".format(sRepeat, sPause, sTune, sBaud + 1)

    tail_conn_air = "{},1,{};".format(txversion, sSpeed_conn_air)
    tail_ITGW = "{},{},0".format(txversion, sSpeed_ITGW)

    # Values of high and low bits (binary -> encoded)
    # bit_low:  0 -> 1 | bit_high: 1 -> 3
    lo = "1,"
    hi = "3,"

    seq_low = hi + hi + lo + lo
    seq_high = hi + lo + hi + lo

    # These sequences are the commands for switching a device on or off
    # On:  01011 -> encoded: 13133
    # Off: 10010 -> encoded: 31131
    on = lo + hi + lo + hi + hi
    off = hi + lo + lo + hi + lo

# TODO implement missing methods
# See here
# https://github.com/Power-Switch/PowerSwitch_Android/blob/master/Smartphone/src/main/java/eu/power_switch/obj/receiver/device/intertechno/CMR1000.java
