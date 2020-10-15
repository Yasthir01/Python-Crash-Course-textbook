def city_country(city, country, population=0):
	"""Return a string like 'Pietermaritzburg, South Africa'."""
	output_string = f"{city.title()}, {country.title()}"
	if population:
		output_string += f" - population = {population}"
	return output_string



