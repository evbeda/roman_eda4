import unittest

from decimal_to_roman import decimal_to_roman


class TestDecimalToRoman(unittest.TestCase):

    def test_decimal_to_roman_0(self):
        result = decimal_to_roman(0)
        self.assertEquals(result, '')

    def test_decimal_to_roman_1(self):
        result = decimal_to_roman(1)
        self.assertEquals(result, 'I')

    #kcasckas
if __name__ == "__main__":
    unittest.main()
