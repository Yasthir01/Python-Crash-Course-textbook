class Users:
	"""	A class representing user profiles"""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the user"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attempts = 0

	def describe_user(self):
		"""Summary of the user profile"""
		print(f"\n{self.first_name} {self.last_name}")
		print(f"\tUsername: {self.username}")
		print(f"\tEmail: {self.email}")
		print(f"\tLocation: {self.location}")

	def greet_user(self):
		"""Personalized greeting to the user"""
		print(f"\nWelcome back, {self.username}")

	def increment_login_attempts(self):
		"""Increment the login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts to 0"""
		self.login_attempts = 0 


#First User
yasthir = Users('yasthir', 'dhewnarian', 'yasthird001', 'yasthir007@gmail.com',
				'pietermaritzburg')

yasthir.describe_user()
yasthir.greet_user()

#Second User
dineesha = Users('dineesha', 'singh', 'dinz001', 'dinsingh@outlook.com',
				'durban')

dineesha.describe_user()
dineesha.greet_user()

print("\nMaking 3 login attempts...")
dineesha.increment_login_attempts()
dineesha.increment_login_attempts()
dineesha.increment_login_attempts()
dineesha.increment_login_attempts()
print(f"Login Attempts: {dineesha.login_attempts}")

print("***Resetting login attempts...")
dineesha.reset_login_attempts()
print(f"Login Attempts: {dineesha.login_attempts}")






