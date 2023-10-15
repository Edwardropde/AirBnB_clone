#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """Test Amenity class attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """Test string representation of Amenity instance"""
        amenity = Amenity()
        self.assertTrue("[Amenity]" in str(amenity))


if __name__ == "__main__":
    unittest.main()
