import unittest

from decimal_to_roman import decimal_to_roman


class TestDecimalToRoman(unittest.TestCase):

    def test_decimal_to_roman_0(self):
        result = decimal_to_roman(0)
        self.assertEquals(result, '')

    def test_decimal_to_roman_1(self):
        result = decimal_to_roman(1)
        self.assertEquals(result, 'I')

    def test_decimal_to_roman_2(self):
        result = decimal_to_roman(2)
        self.assertEquals(result, 'II')

    def test_decimal_to_roman_3(self):
        result = decimal_to_roman(3)
        self.assertEquals(result, 'III')

    def test_decimal_to_roman_4(self):
        result = decimal_to_roman(4)
        self.assertEquals(result, 'IV')

    def test_decimal_to_roman_5(self):
        result = decimal_to_roman(5)
        self.assertEquals(result, 'V')
    def test_decimal_to_roman_6(self):
        result = decimal_to_roman(6)
        self.assertEquals(result, 'VI')
    def test_decimal_to_roman_7(self):
        result = decimal_to_roman(7)
        self.assertEquals(result, 'VII')
    def test_decimal_to_roman_8(self):
        result = decimal_to_roman(8)
        self.assertEquals(result, 'VIII')
    def test_decimal_to_roman_9(self):
        result = decimal_to_roman(9)
        self.assertEquals(result, 'IX')
    def test_decimal_to_roman_10(self):
        result = decimal_to_roman(10)
        self.assertEquals(result, 'X')

    def test_decimal_to_roman_11(self):
        result = decimal_to_roman(11)
        self.assertEquals(result, 'XI')

    def test_decimal_to_roman_12(self):
        result = decimal_to_roman(12)
        self.assertEquals(result, 'XII')

    def test_decimal_to_roman_13(self):
        result = decimal_to_roman(13)
        self.assertEquals(result, 'XIII')

    def test_decimal_to_roman_14(self):
        result = decimal_to_roman(14)
        self.assertEquals(result, 'XIV')

    def test_decimal_to_roman_15(self):
        result = decimal_to_roman(15)
        self.assertEquals(result, 'XV')

    def test_decimal_to_roman_16(self):
        result = decimal_to_roman(16)
        self.assertEquals(result, 'XVI')

    def test_decimal_to_roman_17(self):
        result = decimal_to_roman(17)
        self.assertEquals(result, 'XVII')

    def test_decimal_to_roman_18(self):
        result = decimal_to_roman(18)
        self.assertEquals(result, 'XVIII')

    def test_decimal_to_roman_19(self):
        result = decimal_to_roman(19)
        self.assertEquals(result, 'XIX')

    def test_decimal_to_roman_20(self):
        result = decimal_to_roman(20)
        self.assertEquals(result, 'XX')




if __name__ == "__main__":
    unittest.main()
