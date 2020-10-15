import unittest

from employee import Employee 

class TestEmployee(unittest.TestCase):
	"""tests for the module employee.py"""

	def setUp(self):
		"""Make an employee to use in tests"""
		self.yash = Employee('yash', 'dhewnarian', 65000)

	def test_give_default_raise(self):
		"""Test that a defualt raise works correctly"""
		self.yash.give_raise()
		self.assertEqual(self.yash.salary, 70000)

	def test_give_custom_raise(self):
		"""Test that a custom raise works correctly"""
		self.yash.give_raise(10000)
		self.assertEqual(self.yash.salary, 75000)


if __name__ == '__main__':
	unittest.main()