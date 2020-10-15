import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do city and country pairs like Durban, 'South Africa' work?"""
		city_country_pair = city_country('durban', 'south africa')
		self.assertEqual(city_country_pair, 'Durban, South Africa')


	def test_city_country_population(self):
		"""Can I include a population argument?"""
		city_country_pair = city_country('durban', 'south africa', population=5_000_000)
		self.assertEqual(city_country_pair, 'Durban, South Africa - population = 5000000')



if __name__ == '__main__':
	unittest.main()