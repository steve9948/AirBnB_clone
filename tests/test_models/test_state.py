#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''Class state test case'''

    def setUp(self):
        self.state = State

    def test_default_values(self):
        # Check if the default values are set correctly
        self.assertEqual(self.state.name, "")

    def test_set_values(self):
        # Test setting values and checking if they are stored correctly
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
