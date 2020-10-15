from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	#Get a first name
	first = input("What is your first name? ")
	if first == 'q':
		break
	#Get a last name
	last = input("What is your last name?")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tNeatly formatted name: {formatted_name}")
	