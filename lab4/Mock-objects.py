import sys
sys.path.insert(0, "C:/Users/Andrew/Desktop/BKIT_UNIVERSITY/lab1")

import unittest
from unittest.mock import Mock
from qr import get_roots

class TestQr(unittest.TestCase):
	def test_get_roots(self):
		mockRoot = Mock(return_value = 412)
		get_roots(mockRoot(), 2, 1)


if __name__ == "__main__":
	unittest.main()