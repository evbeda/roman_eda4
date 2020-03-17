import unittest

from decimal_to_roman import decimal_to_roman


class TestDecimalToRoman(unittest.TestCase):

    def test_decimal_to_roman_1(self):
        result = decimal_to_roman(1)
        self.assertEquals(result, 'I')


    def test_roman_to_decimal_1(self):
        result = roman_to_decimal("I")
        self.assertEqual(result, 1)

    def test_roman_to_decimal_2(self):
        result = roman_to_decimal("II")
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
