import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does 'Santiago, Chile' work?"""
        city_country_name = city_country('santiago', 'chile')
        self.assertEqual(city_country_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does 'Santiago, Chile, population=5000000' work?"""
        city_country_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(city_country_name, 'Santiago, Chile - population 5000000')

if __name__ == "__main__":
    unittest.main()