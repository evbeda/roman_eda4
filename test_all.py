import unittest

from decimal_to_roman import DecimalToRoman
from roman_to_decimal import roman_to_decimal


class TestAll(unittest.TestCase):

    def test_all(self):
        for number in range(1, 4000):
            d_to_r = DecimalToRoman()
            print(number)
            roman = d_to_r.decimal_to_roman(number)
            print(roman)
            result_number = roman_to_decimal(roman)
            print(result_number)
            self.assertEquals(number, result_number)


if __name__ == "__main__":
    unittest.main()
