#!/usr/bin/python3
import unittest
from models.engine.file_storage import storage


class TestFileStorageReload(unittest.TestCase):

    def setUp(self):
        # Ensure a clean slate for each test
        storage.reload()

    def test_reload_empty(self):
        # Test reloading when the storage is initially empty
        storage.reload()
        # Assert any expectations based on the state after reloading

    def test_reload_with_data(self):
        # Test reloading when the storage contains some data
        # You can add objects to storage before calling reload
        # storage["some_key"] = some_object
        storage.reload()
        # Assert any expectations based on the state after reloading


if __name__ == '__main__':
    unittest.main()
