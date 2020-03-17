
class DecimalToRoman():

	def __init__(self):
		self.response = ""


	def decimal_to_roman(self, number):
		if (number >= 10):
			self.response += 'X'
			return self.decimal_to_roman(number - 10)
		elif (number >= 5):
			if number == 9:
				self.response += 'IX'
				return self.decimal_to_roman(number - 9)
			else:
				self.response += 'V'
				return self.decimal_to_roman(number - 5)
		elif number >= 1:
			if number == 4:
				self.response += 'IV'
				return self.decimal_to_roman(number - 4)
			else:
				self.response += "I"
				return self.decimal_to_roman(number - 1)
		elif number <= 0:
			return self.response