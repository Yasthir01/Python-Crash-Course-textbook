filename = 'guest_book.txt'

while True:
	name = input("Please enter your name.\nType ('quit') to exit: ")
	if name == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(f"{name}\n")
		print(f"Hi, {name}... You have been added to the guest book!")

