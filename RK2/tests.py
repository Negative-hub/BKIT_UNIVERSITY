import unittest
import main

class Test_main(unittest.TestCase):
	def test_task1(self):
		self.assertEqual(main.task1(), 
		[('Титов', ['Процессор', 'Кулер', 'Монитор']), ('Бения', ['Жесткий диск'])])
	
	def test_task2(self):
		self.assertEqual(main.task2(),
		[('Бения', 9000.0), ('Титов', 12666.67), ('Яковенко', 15000.0)])

	def test_task3(self):
		self.assertEqual(main.task3(),
		[('Материнская плата', ['Яковенко', 'Васильев']), ('Монитор', ['Бения'])])

if __name__ == "__main__":
	unittest.main()