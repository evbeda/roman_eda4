import unittest

from roman_to_decimal import roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):

    def test_roman_to_decimal_1(self):
        result = roman_to_decimal("I")
        self.assertEqual(result, 1)


    def test_roman_to_decimal_2(self):
        result = roman_to_decimal("II")
        self.assertEqual(result, 2)

    def test_roman_to_decimal_3(self):
        result = roman_to_decimal("III")
        self.assertEqual(result, 3)

    def test_roman_to_decimal_3(self):
        result = roman_to_decimal("V")
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
