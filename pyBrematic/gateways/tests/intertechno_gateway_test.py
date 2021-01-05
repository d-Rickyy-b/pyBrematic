# -*- coding: utf-8 -*-
import socket
import unittest
from unittest.mock import Mock, patch

from pyBrematic import Action
from pyBrematic.gateways import IntertechnoGateway


class TestIntertechnoGateway(unittest.TestCase):

    def setUp(self):
        self.ip = "192.168.1.100"
        self.port = "1234"
        self.gw = IntertechnoGateway(self.ip, self.port)

    def test_default_port(self):
        """Test if default port is correctly set"""
        self.gw = IntertechnoGateway(self.ip)
        self.assertEqual(49880, self.gw._port)

    def test_build_udp_payload(self):
        """Test if building the UDP payload for the Intertechno GW works correctly"""
        device = Mock()
        device.repeat = 2345
        device.pause_BS = 917
        device.pause_IT = 111
        device.tune = 557
        device.baud = 91919
        device.txversion = 1
        device.speed_BS = 234
        device.speed_IT = 432

        function = Mock()
        function.return_value = "A,SIGNAL-A,B,B,A-SIGNAL,C"
        device.get_signal = function

        payload = self.gw.build_udp_payload(device, Action.ON)
        self.assertEqual("0,0,2345,111,557,91919,A,SIGNAL-A,B,B,A-SIGNAL,C,1,432", payload)

    def test_get_head(self):
        """Test if formatting the 'head' string works with random data"""
        self.gw.head_format = "1{0}----{1}++++{2}ASDF{3}#24/"
        head = self.gw.get_head(777, "ASDF1", 313, "-A-")
        self.assertEqual("1777----ASDF1++++313ASDF-A-#24/", head)

    def test_get_tail(self):
        """Test if formatting the 'tail' string works with random data"""
        self.gw.tail_format = "1{0}---++---{1}++ASDF#24/"
        tail = self.gw.get_tail("//-ASDF1", 313)
        self.assertEqual("1//-ASDF1---++---313++ASDF#24/", tail)

    def test_missing_head_format(self):
        """Test if missing 'head' format is handled correctly"""
        self.gw.head_format = None
        with self.assertRaises(ValueError):
            _ = self.gw.get_head("1", "2", "3", "4")

    def test_invalid_tail_format(self):
        """Test if missing 'tail' format is handled correctly"""
        self.gw.tail_format = None
        with self.assertRaises(ValueError):
            _ = self.gw.get_tail("1", "2")

    @patch("socket.socket")
    def test_send_request(self, socket_class_mock):
        device_mock = Mock()
        # Mock method to prevent issues with that
        build_udp_payload_mock = Mock()
        payload_mock = Mock()
        # Since "encode" is being called on the payload object later on, we need to set a return value
        payload_mock.encode.return_value = "Test Payload"
        build_udp_payload_mock.return_value = payload_mock
        self.gw.build_udp_payload = build_udp_payload_mock
        action_mock = Mock()

        socket_instance_mock = Mock()
        socket_class_mock.return_value = socket_instance_mock

        self.gw.send_request(device_mock, action_mock)

        build_udp_payload_mock.assert_called_once_with(device_mock, action_mock)

        socket_class_mock.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)
        socket_instance_mock.sendto.assert_called_once_with("Test Payload", (self.ip, self.port))

if __name__ == '__main__':
    unittest.main()
