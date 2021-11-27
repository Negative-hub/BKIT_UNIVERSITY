import sys
sys.path.insert(0, "C:/Users/Andrew/Desktop/BKIT_UNIVERSITY/lab1")

import unittest
from qr import get_roots

class TestGetRoots(unittest.TestCase):
	def testGetRoots(self):
		self.assertEqual(get_roots(1, -10, 21), [7, 3])
		self.assertEqual(get_roots(1, 2, 1), [-1])

if __name__ == "__main__":
	unittest.main()