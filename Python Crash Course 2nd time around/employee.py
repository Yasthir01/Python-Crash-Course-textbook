class Employee:
	"""A class to represent an employee"""

	def __init__(self, f_name, l_name, salary):
		"""Initalize the employee"""
		self.first = f_name
		self.last = l_name
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Give the employee a raise"""
		self.salary += amount
