import unittest

from pyBrematic.devices.intertechno.tools import calc_unitcode, calc_systemcode, calc_system_and_unit_code


class TestIntertechnoTools(unittest.TestCase):

    def test_calc_unitcode_invalid_range(self):
        """Test if exception raises on out of range values for calc_unitcode"""
        with self.assertRaises(expected_exception=ValueError):
            calc_unitcode(-1)

        with self.assertRaises(expected_exception=ValueError):
            calc_unitcode(17)

    def test_calc_systemcode_invalid_range(self):
        """Test if exception raises on out of range values for calc_systemcode"""
        with self.assertRaises(expected_exception=ValueError):
            calc_systemcode("Z")

        with self.assertRaises(expected_exception=ValueError):
            calc_systemcode("-")

        with self.assertRaises(expected_exception=ValueError):
            calc_systemcode("")

    def test_calc_systemcode(self):
        """Test if the system code calculation returns correct codes"""
        code = calc_systemcode("A")
        self.assertEqual(code, "0000")
        code = calc_systemcode("B")
        self.assertEqual(code, "1000")
        code = calc_systemcode("C")
        self.assertEqual(code, "0100")
        code = calc_systemcode("D")
        self.assertEqual(code, "1100")
        code = calc_systemcode("E")
        self.assertEqual(code, "0010")
        code = calc_systemcode("F")
        self.assertEqual(code, "1010")
        code = calc_systemcode("G")
        self.assertEqual(code, "0110")
        code = calc_systemcode("H")
        self.assertEqual(code, "1110")
        code = calc_systemcode("I")
        self.assertEqual(code, "0001")
        code = calc_systemcode("J")
        self.assertEqual(code, "1001")
        code = calc_systemcode("K")
        self.assertEqual(code, "0101")
        code = calc_systemcode("L")
        self.assertEqual(code, "1101")
        code = calc_systemcode("M")
        self.assertEqual(code, "0011")
        code = calc_systemcode("N")
        self.assertEqual(code, "1011")
        code = calc_systemcode("O")
        self.assertEqual(code, "0111")
        code = calc_systemcode("P")
        self.assertEqual(code, "1111")

    def test_calc_unitcode(self):
        """Test if the unit code calculation returns correct codes"""
        code = calc_unitcode(1)
        self.assertEqual(code, "0000")
        code = calc_unitcode(2)
        self.assertEqual(code, "1000")
        code = calc_unitcode(3)
        self.assertEqual(code, "0100")
        code = calc_unitcode(4)
        self.assertEqual(code, "1100")
        code = calc_unitcode(5)
        self.assertEqual(code, "0010")
        code = calc_unitcode(6)
        self.assertEqual(code, "1010")
        code = calc_unitcode(7)
        self.assertEqual(code, "0110")
        code = calc_unitcode(8)
        self.assertEqual(code, "1110")
        code = calc_unitcode(9)
        self.assertEqual(code, "0001")
        code = calc_unitcode(10)
        self.assertEqual(code, "1001")
        code = calc_unitcode(11)
        self.assertEqual(code, "0101")
        code = calc_unitcode(12)
        self.assertEqual(code, "1101")
        code = calc_unitcode(13)
        self.assertEqual(code, "0011")
        code = calc_unitcode(14)
        self.assertEqual(code, "1011")
        code = calc_unitcode(15)
        self.assertEqual(code, "0111")
        code = calc_unitcode(16)
        self.assertEqual(code, "1111")

    def test_calc_system_and_unit_code(self):
        """Test if combined method does exactly the same as the individual methods"""
        system1, unit1 = calc_system_and_unit_code("A5")
        self.assertEqual(system1, calc_systemcode("A"))
        self.assertEqual(unit1, calc_unitcode(5))

        system2, unit2 = calc_system_and_unit_code("B11")
        self.assertEqual(system2, calc_systemcode("B"))
        self.assertEqual(unit2, calc_unitcode(11))

        system3, unit3 = calc_system_and_unit_code("F8")
        self.assertEqual(system3, calc_systemcode("F"))
        self.assertEqual(unit3, calc_unitcode(8))

    def test_calc_system_and_unit_code_issue(self):
        """Test if wrong input raises a ValueError"""
        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("Q5")

        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("R18")

        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("A18")

        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("A0101110101")

        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("11B")

        with self.assertRaises(ValueError):
            _, _ = calc_system_and_unit_code("0000100001")


if __name__ == "__main__":
    unittest.main()
