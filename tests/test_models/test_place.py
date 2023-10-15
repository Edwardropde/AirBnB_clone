#!/usr/bin/python3


import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_attributes(self):
        """Test Place class attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str_representation(self):
        """Test string representation of Place instance"""
        place = Place()
        self.assertTrue("[Place]" in str(place))


if __name__ == "__main__":
    unittest.main()
