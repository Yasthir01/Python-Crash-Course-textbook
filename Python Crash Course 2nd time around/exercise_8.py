# def city_country(city, country):
# 	"""Returns a city and its country"""
# 	return f"{city.title()}, {country.title()}"



# def make_album(artist, title, songs=None):
# 	"""Builds a dictionary containing information about an album"""
# 	album_dict = {
# 		'artist': artist.title(),
# 		'title': title.title(),
# 		}
# 	if songs:
# 		album_dict['songs'] = songs
# 	return album_dict

# # Prepare the prompts
# title_prompt = "\nWhat album are you thinking of?"
# artist_prompt = "Who's the artist?"

# #Let the user know how to quit
# print("Enter 'quit' at any time to quit ")

# while True:
# 	title = input(title_prompt)
# 	if title == 'quit':
# 		break

# 	artist = input(artist_prompt)
# 	if artist == 'quit':
# 		break

# 	album = make_album(artist, title)
# 	print(album)

# print("\nThanks for reponding!")


# print("--------------------------------------------------")

# def show_messages(messages):
# 	"""Prints all messages in a list"""
# 	print("Showing all messages")
# 	for message in messages:
# 		print(message)

# def send_messages(messages, sent_messages):
# 	"""Print each message, and then send it to sent_messages"""
# 	print("\nSending all messages...")
# 	while messages:
# 		current_message = messages.pop()
# 		print(current_message)
# 		sent_messages.append(current_message)


# messages = ["Hello little one", "How are you today?", "Otaaayyyyy"]
# show_messages(messages)

# sent_messages = []
# send_messages(messages[:], sent_messages)

# print("\nFinal Lists: ")
# print(messages)
# print(sent_messages)


def make_sandwich(*items):
	"""Summary of the sandwich being ordered"""
	print("I'm about to make you a Sandwich!")
	print("----------------------------------")
	for item in items:
		print(f"-Adding {item} to your sandwich...")
	print("----------------------------------")
	print("Your sandwich is ready!")

make_sandwich('ham', 'cheese', 'onions')

