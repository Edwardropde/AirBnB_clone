#!/usr/bin/python3

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes(self):
        city = City()
        city.state_id = "CA"
        city.name = "Los Angeles"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "Los Angeles")


if __name__ == '__main__':
    unittest.main()
