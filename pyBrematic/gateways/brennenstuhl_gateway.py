import socket

from pyBrematic.gateways.gateway import Gateway


# http://luckow.org/archive/brennenstuhl.html

class BrennenstuhlGateway(Gateway):

    # Method for encoding the system_code or unit_code from binary to a gateway-readable format
    @staticmethod
    def encode_code(code, seq_low, seq_high):
        encoded_msg = ""
        for bit in code:
            if bit == "0":
                encoded_msg += seq_low
            elif bit == "1":
                encoded_msg += seq_high
            else:
                raise ValueError("Invalid value in system_code or unit_code!")
        return encoded_msg

    def send_request(self, device, action):
        # Syntax of the request is:
        # |-------Header--------|                                                      |-tail-|
        # TXP:0,0,10,5600,350,25,<bit_low>,<enc_system_code>,<enc_unit_code>,<bit_high>,1,1,16;
        # Check http://luckow.org/archive/brennenstuhl.html (german) for more info about this.

        # Parameters for the requests. Only change if you have good reasons for it
        sRepeat = 10
        sPause = 5600
        sTune = 350
        sBaud = 25
        sSpeed = 16
        txversion = 1

        # Values of high and low bits (binary -> encoded)
        # bit_low:  0 -> 1
        # bit_high: 1 -> 3
        bit_low = 1
        bit_high = 3

        # These sequences are the commands for switching a device on or off
        # On:  01011 -> encoded: 13133
        # Off: 10010 -> encoded: 31131
        ON_SEQ = "1,3,1,3,3"
        OFF_SEQ = "3,1,1,3,1"

        seq_low = "3,3,1,1,"  # bit_high, bit_high, bit_low, bit_low
        seq_high = "3,1,3,1,"  # bit_high, bit_low, bit_high, bit_low

        head = "TXP:0,0,{},{},{},{},".format(sRepeat, sPause, sTune, sBaud)
        tail = ",{},1,{};".format(txversion, sSpeed)

        # Encoding the system_code and unit_code
        system_msg = self.encode_code(device.system_code, seq_low, seq_high)
        unit_msg = self.encode_code(device.unit_code, seq_low, seq_high)

        # Build the payload of the UDP package depending on the action.
        if action == device.ACTION_ON:
            data = head + str(bit_low) + "," + system_msg + unit_msg + str(bit_high) + "," + ON_SEQ + tail
        elif action == device.ACTION_OFF:
            data = head + str(bit_low) + "," + system_msg + unit_msg + str(bit_high) + "," + OFF_SEQ + tail
        else:
            raise ValueError("Value of 'action' isn't valid!")

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(data.encode(), (self._ip, self._port))
        s.close()
