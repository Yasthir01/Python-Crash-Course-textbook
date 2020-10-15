from random import randint

class Die:
	"""A representation of a dice"""

	def __init__(self, sides=6):
		"""Initalize the dice"""
		self.sides = sides


	def roll_die(self):
		"""Return a number between 1 and the number of sides"""
		return randint(1, self.sides)

#Make a 6 sided die and roll it 10 times
d6 = Die()

results = []

for roll in range(10):
	result = d6.roll_die()
	results.append(result)
print("10 Rolls of a 6-sided Die: ")
print(f"\t{results}")


#Make a 10 sided die and roll it 10 times
d10 = Die(10)

results = []

for roll in range(10):
	result = d10.roll_die()
	results.append(result)
print("10 Rolls of a 10-sided Die: ")
print(f"\t{results}")


#Make a 20 sided die and roll it 10 times.
d20 = Die(20)

results = []

for roll in range(10):
	result = d20.roll_die()
	results.append(result)
print("10 Rolls of a 20-sided Die: ")
print(f"\t{results}")

