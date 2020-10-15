"""A set of classes used to represent gas and electric cars"""

class Car:
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize the attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Returns a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Hey, buster! You can't roll back an odomter!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odomter reading"""
		self.odometer_reading += miles


class Battery:
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=75):
		"""Initalize the battery's attributes"""
		self.battery_size = battery_size


	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print(f"This car has a {self.battery_size}-kWH battery")


	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 75:
			battery_range = 260
		elif self.battery_size == 100:
			battery_range = 315

		print(f"This car can go about {battery_range} miles on a full charge.")






class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric cars"""

	def __init__(self, make, model, year):
		"""
		Initalize attributes of the parent class.
		Then initalize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	

# my_used_car = Car('vivo street', 'polo', 2016)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


