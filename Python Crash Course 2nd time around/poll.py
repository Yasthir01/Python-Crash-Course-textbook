filename = 'poll_results.txt'

while True:
	question = input("What do you like about feet?\nType 'quit' to exit: ")
	if question == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(f"{question}\n")
		print("Thanks for the response!")
