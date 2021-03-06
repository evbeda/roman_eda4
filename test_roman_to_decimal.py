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
    
    def test_roman_to_decimal_14(self):
        result = roman_to_decimal("XIV")
        self.assertEqual(result, 14)   
    
    def test_roman_to_decimal_15(self):
        result = roman_to_decimal("XV")
        self.assertEqual(result, 15)

    def test_roman_to_decimal_19(self):
        result = roman_to_decimal("XIX")
        self.assertEqual(result, 19)

    def test_roman_to_decimal_28(self):
        result = roman_to_decimal("XXVIII")
        self.assertEqual(result, 28)

    def test_roman_to_decimal_3191(self):
        result = roman_to_decimal("MMMCXCI")
        self.assertEqual(result, 3191)

    def test_roman_to_decimal_94(self):
        result = roman_to_decimal("XCIV")
        self.assertEqual(result, 94)

if __name__ == "__main__":
    unittest.main()
