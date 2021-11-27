import unittest
import bot

class TestBot(unittest.TestCase):
	def testOperation(self):
		bot.first_num("6")
		bot.second_num("6")

		self.assertEqual(bot.operation("*"), 36)
		self.assertEqual(bot.operation("+"), 12)

if __name__ == "__main__":
	unittest.main()