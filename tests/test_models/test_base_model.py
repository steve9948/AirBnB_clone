#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_uuid_generation(self):
        # create two instances
        instance1 = BaseModel()
        instance2 = BaseModel()
        # check if the id exists
        self.assertTrue(hasattr(instance1, 'id'))
        self.assertTrue(hasattr(instance2, 'id'))
        # check if id is unique for each instance
        self.assertNotEqual(instance1.id, instance2.id)

    def test_object_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_str_method(self):
        instance = BaseModel()
        instance_str = str(instance)
        expected_str = "[BaseModel] ({}) {}".format(
            instance.id, instance.__dict__)
        self.assertEqual(instance_str, expected_str)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
