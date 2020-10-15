"""A class representing a restaurant"""

class Restaurant:
	"""A class representing a restaurant"""

	def __init__(self, name, cuisine_type):
		"""Initialize the restaurant"""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		"""Display a sumary of the restaurant"""
		print(f"{self.name} serves {self.cuisine_type}\n")

	def open_restaurant(self):
		"""Displays a message that the restaurant is open"""
		print(f"{self.name} is open! Come on in!")

	def set_number_served(self, number_served):
		"""Allows a user to set the number of customers served"""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served"""
		self.number_served += additional_served


# panarottis = Restaurant('panarottis', 'pizza')
# panarottis.describe_restaurant()

# burger_king = Restaurant('burger king', 'burgers')
# burger_king.describe_restaurant()

# mugg_and_bean = Restaurant('mugg & bean', 'coffee')
# mugg_and_bean.describe_restaurant()

# restaurant = Restaurant('wimpy', 'breakfast')
# restaurant.describe_restaurant()

# print(f"Number Served: {restaurant.number_served}")
# restaurant.number_served = 50
# print(f"Number Served: {restaurant.number_served}")

# restaurant.set_number_served(23)
# print(f"Number Served: {restaurant.number_served}")

# restaurant.increment_number_served(45)
# print(f"{restaurant.number_served} customers served in a day of business")






