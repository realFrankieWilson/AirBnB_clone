#!/usr/bin/python3


"""
This module contains all the test cases for the City class attributes
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """ Test cases for the City class in the models/city module"""

    def setUp(self):
        self.city = City()

    def test_City_is_BaseModel_subclass(self):
        """
        Verify City class is a subclass of BaseModel
        """
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_if_class_attributes_exit(self):
        """Verify City class has name and state_id attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_class_attribute_type_and_initials(self):
        """
        Verify 'name' and 'state_id' attributes have correct
        data types and initial values.
        """
        self.assertIs(type(self.city.name), str)
        self.assertIs(type(self.city.state_id), str)
        self.assertTrue(self.city.name == "")
        self.assertTrue(self.city.state_id == "")
        self.assertFalse(bool(self.city.name))
        self.assertFalse(bool(self.city.state_id))
