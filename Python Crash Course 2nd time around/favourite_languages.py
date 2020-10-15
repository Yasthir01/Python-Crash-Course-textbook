favourite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favourite_languages.items():
	print(f"\n{name.title()}'s favourite languages are: ")
	for language in languages:
		print(f"\t{language.title()}")

