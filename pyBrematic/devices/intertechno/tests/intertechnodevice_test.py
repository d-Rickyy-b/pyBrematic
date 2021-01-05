# -*- coding: utf-8 -*-

import unittest

from pyBrematic.devices.intertechno import IntertechnoDevice


class TestIntertechnoDevice(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_unitcode_invalid_range(self):
        """Test if exception raises on out of range values for calc_unitcode"""
        with self.assertRaises(expected_exception=ValueError):
            IntertechnoDevice.calc_unitcode(-1)

        with self.assertRaises(expected_exception=ValueError):
            IntertechnoDevice.calc_unitcode(17)

    def test_calc_systemcode_invalid_range(self):
        """Test if exception raises on out of range values for calc_systemcode"""
        with self.assertRaises(expected_exception=ValueError):
            IntertechnoDevice.calc_systemcode("Z")

        with self.assertRaises(expected_exception=ValueError):
            IntertechnoDevice.calc_systemcode("-")

        with self.assertRaises(expected_exception=ValueError):
            IntertechnoDevice.calc_systemcode("")

    def test_calc_systemcode(self):
        """Test if the system code calculation returns correct codes"""
        dev = IntertechnoDevice("0000", "0000")

        code = dev.calc_systemcode("A")
        self.assertEqual(code, "0000")
        code = dev.calc_systemcode("B")
        self.assertEqual(code, "1000")
        code = dev.calc_systemcode("C")
        self.assertEqual(code, "0100")
        code = dev.calc_systemcode("D")
        self.assertEqual(code, "1100")
        code = dev.calc_systemcode("E")
        self.assertEqual(code, "0010")
        code = dev.calc_systemcode("F")
        self.assertEqual(code, "1010")
        code = dev.calc_systemcode("G")
        self.assertEqual(code, "0110")
        code = dev.calc_systemcode("H")
        self.assertEqual(code, "1110")
        code = dev.calc_systemcode("I")
        self.assertEqual(code, "0001")
        code = dev.calc_systemcode("J")
        self.assertEqual(code, "1001")
        code = dev.calc_systemcode("K")
        self.assertEqual(code, "0101")
        code = dev.calc_systemcode("L")
        self.assertEqual(code, "1101")
        code = dev.calc_systemcode("M")
        self.assertEqual(code, "0011")
        code = dev.calc_systemcode("N")
        self.assertEqual(code, "1011")
        code = dev.calc_systemcode("O")
        self.assertEqual(code, "0111")
        code = dev.calc_systemcode("P")
        self.assertEqual(code, "1111")

    def test_calc_unitcode(self):
        """Test if the unit code calculation returns correct codes"""
        dev = IntertechnoDevice("0000", "0000")

        code = dev.calc_unitcode(1)
        self.assertEqual(code, "0000")
        code = dev.calc_unitcode(2)
        self.assertEqual(code, "1000")
        code = dev.calc_unitcode(3)
        self.assertEqual(code, "0100")
        code = dev.calc_unitcode(4)
        self.assertEqual(code, "1100")
        code = dev.calc_unitcode(5)
        self.assertEqual(code, "0010")
        code = dev.calc_unitcode(6)
        self.assertEqual(code, "1010")
        code = dev.calc_unitcode(7)
        self.assertEqual(code, "0110")
        code = dev.calc_unitcode(8)
        self.assertEqual(code, "1110")
        code = dev.calc_unitcode(9)
        self.assertEqual(code, "0001")
        code = dev.calc_unitcode(10)
        self.assertEqual(code, "1001")
        code = dev.calc_unitcode(11)
        self.assertEqual(code, "0101")
        code = dev.calc_unitcode(12)
        self.assertEqual(code, "1101")
        code = dev.calc_unitcode(13)
        self.assertEqual(code, "0011")
        code = dev.calc_unitcode(14)
        self.assertEqual(code, "1011")
        code = dev.calc_unitcode(15)
        self.assertEqual(code, "0111")
        code = dev.calc_unitcode(16)
        self.assertEqual(code, "1111")


if __name__ == "__main__":
    unittest.main()
