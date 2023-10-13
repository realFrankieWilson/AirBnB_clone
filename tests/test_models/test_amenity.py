#!/usr/bin/python3


"""
This module contains all the test cases for the Amenity class attributes
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ Test cases for the Amenity class in the models/amenity module"""
    
    def setUp(self):
        self.amenity = Amenity()

    def test_Amenity_is_BaseModule_subclass(self):
        """ 
        Verify Amenity class is a subclass of BaseModel
        """
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_if_class_attribute_exit(self):
        """Verify Amenity class has name attribute"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_class_attribute_type_and_initials(self):
        """
        Verify 'name' attribute have correct
        data types and initial values.
        """
        self.assertIs(type(self.amenity.name), str)
        self.assertTrue(self.amenity.name == "")
        self.assertFalse(bool(getattr(self.amenity, 'name')))
