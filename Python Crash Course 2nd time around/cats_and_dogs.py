filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	
	try:
		with open(filename) as f:
			contents = f.read()
			

	except FileNotFoundError:
		passN

	else:
		print(f"\nReading File: {filename}")
		print(contents.title())


