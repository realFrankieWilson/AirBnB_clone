#!/usr/bin/python3


"""
This module contains all the test cases for the Place class attributes.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ Test cases against the Place class in the models/place module"""

    def setUp(self):
        self.place = Place()
        self.attr_lst = ["name", "city_id", "user_id", "description",
                         "number_rooms", "number_bathrooms", "max_guest",
                         "price_by_night", "latitude", "longitude",
                         "amenity_ids"]

    def test_if_class_attribute_exit(self):
        """Verify Place class has attributes in the self.attr_lst"""
        for attr in self.attr_lst:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attributes_type_and_initials(self):
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attr in self.attr_lst:
            self.assertFalse(bool(getattr(self.place, attr)))

    def test_Place_is_BaseModule_subclass(self):
        self.assertTrue(issubclass(type(self.place), BaseModel))
