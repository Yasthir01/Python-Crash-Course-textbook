def describe_pet(pet_name, animal_type= 'dog'):
	"""Display information about a pet"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

def make_shirt(size, text_on_shirt):
	"""Displays the size of shirt and text displayed on it"""
	print(f"The size of the shirt is a {size.title()} and the text says {text_on_shirt.title()}")

def describe_city(city, country= 'america'):
	"""Describes a city and it's country"""
	print(f"{city.title()} is in {country.title()}")



describe_pet(animal_type='tiger', pet_name='tanya')
print()
describe_pet(pet_name= 'tanya')

make_shirt('medium', 'boogey woogey woogey')
make_shirt(size = 'medium', text_on_shirt= 'outdoor man')

describe_city('pmb', 'south africa')
describe_city('durban')




