#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attributes(self):
        """Test Review class attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        """Test string representation of Review instance"""
        review = Review()
        self.assertTrue("[Review]" in str(review))


if __name__ == "__main__":
    unittest.main()
