#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''Class amenity test case'''

    def setUp(self):
        self.amenity = Amenity

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.amenity.name, "")

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.amenity.name = "WiFi"
        self.assertEqual(self.amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
