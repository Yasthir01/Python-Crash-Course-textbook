# Prompts for the user's favourite number
import json

number = input("What is your favourite number? ")

filename = 'favourite_number.json'
with open(filename, 'w') as f:
	json.dump(number, f)
	print("Thanks! I will be sure to remember your number!")

