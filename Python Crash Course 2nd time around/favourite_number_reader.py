import json

filename = 'favourite_number.json'

try:
	with open(filename, 'r') as f:
		number = json.load(f)

except FileNotFoundError:
	number = input("What is your favourite number? ")
	with open(filename, 'w') as f:
		json.dump(number, f)
	print("Thanks! I will be sure to remember your number!")

else:
	print(f"I know your favourite number! It is... {number}!")
