# current_number = 0 
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue

# 	print(current_number)

# print("--------------------------")
# x = 1
# while x <= 5:
# 	print(x)
# 	x += 1

# print("--------------------------------")

# prompt = "\nEnter your desired pizza toppings: "
# prompt += "\nEnter 'quit' when you are finished."

# while True:
# 	topping = input(prompt)
# 	if topping != 'quit':
# 		print(f"Adding {topping.title()} to your pizza...")
# 	else:
# 		break


age = int(input("How old are you? *(Enter 'quit' when you're finished."))

while True:
	if age == 'quit':
		break
	#If it is a child less than 3 years old then the ticket is free	
	elif age < 3:
		price = 0
	#If it is a child between 3 and 12 then the price is 10 Dollars	
	elif age > 3 and age < 12:
		price = 10
	#If it is someone 12 years and older then the ticket is 15 Dollars	
	elif age >= 12:
		price = 15

	print(f"Your move ticket based on your age is ${price}")




