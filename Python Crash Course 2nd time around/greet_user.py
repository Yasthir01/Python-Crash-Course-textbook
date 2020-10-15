import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.
def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename, 'r') as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""Prompt for a new username"""
	username = input("What is your name?")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username




def greet_user():
	"""Greet the user by name"""
	username = get_stored_username()
	if username:
		correct = input(f"Are you {username}? (y/n)")
		if correct == 'y':
			print(f"Welcome back, {username}")
		else:
			username = get_new_username()
			print(f"We will remember you when you come back, {username}! :)")

	else:
		username = get_new_username() 
		print(f"We will remember you when you come back, {username}! :)")
		
	

greet_user()


