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

    def test_roman_to_decimal_4(self):
        result = roman_to_decimal("IV")
        self.assertEqual(result, 4)
    
    def test_roman_to_decimal_5(self):
        result = roman_to_decimal("V")
        self.assertEqual(result, 5)

    def test_roman_to_decimal_9(self):
        result = roman_to_decimal("IX")
        self.assertEqual(result, 9)

    def test_roman_to_decimal_10(self):
        result = roman_to_decimal("X")
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
