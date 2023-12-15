#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''Class review test case'''

    def setUp(self):
        self.review = Review

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "A wonderful stay at the cozy cabin!"

        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text,
                         "A wonderful stay at the cozy cabin!")


if __name__ == '__main__':
    unittest.main()
