current_users = ['bob', 'alfred', 'candice', 'tim', 'simone']

new_users = ['fred', 'owen', 'bob', 'abby', 'tim']

for new_user in new_users:
	if new_user in current_users:
		print(f"Sorry, {new_user} has been taken")
	else:
		print(f"{new_user} is avaiable!")


numbers = list(range(1, 10))

for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th")




