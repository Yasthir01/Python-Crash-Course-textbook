import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py"""

	def test_first_last_name(self):
		"""Do names like 'Yasthir Dhewnarian' work?"""
		formatted_name = get_formatted_name('yasthir', 'dhewnarian')
		self.assertEqual(formatted_name, 'Yasthir Dhewnarian')

	def test_first_last_middle_name(self):
		"""Do names like 'Yasthir Yash Dhewnarian' work?"""
		formatted_name = get_formatted_name('yasthir', 'dhewnarian', 'yash')
		self.assertEqual(formatted_name, 'Yasthir Yash Dhewnarian')
		

if __name__ == '__main__':
	unittest.main()

