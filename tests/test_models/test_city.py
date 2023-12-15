#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''Class City test case'''

    def setUp(self):
        self.city = City()

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_inheritance(self):
        # Check if City inherits from BaseModel
        self.assertIsInstance(self.city, BaseModel)


if __name__ == '__main__':
    unittest.main()
