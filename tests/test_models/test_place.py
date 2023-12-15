#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''Class place test case'''

    def setUp(self):
        self.place = Place

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Cozy Cabin"
        self.place.description = "A charming cabin in the woods."
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = [1, 2, 3]

        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.description,
                         "A charming cabin in the woods.")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
