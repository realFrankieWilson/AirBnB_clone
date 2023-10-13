#!/usr/bin/python3

"""
This module contains all the test cases for the User class attributes
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """ Test cases for the User class in the models/user module"""

    def test_if_attributes_exit(self):
        """ Verify User class has 'first_name' and 'last_name' attributes"""
        user_1 = User()
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_class_attributes(self):
        """
        Verify 'first_name' and 'last_name' have correct
        data types and initial values.
        """
        user_1 = User()
        self.assertIs(type(user_1.first_name), str)
        self.assertIs(type(user_1.last_name), str)
        self.assertTrue(user_1.first_name == "")
        self.assertTrue(user_1.last_name == "")

    def test_inheritance(self):
        """
        Verify User class is a subclass of BaseModel.
        """
        user_1 = User()
        self.assertTrue(issubclass(type(user_1), BaseModel))
