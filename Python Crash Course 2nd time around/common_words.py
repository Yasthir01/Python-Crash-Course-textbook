def count_common_words(filename, word):
	"""Count how many times a word appears in a text"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass

	else:
		word_count = contents.lower().count(word)

		message = f"'{word}' appears in {filename} about {word_count} times."
		print(message)

filename = 'alice.txt'
count_common_words(filename, 'the')