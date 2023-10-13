#!/usr/bin/python3


"""
This module contains all the test cases for the User class attributes
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """ Test cases for the State class in the models/state module"""

    def test_state_is_basemodel_subclass(self):
        """ 
        Verify State class is a subclass of BaseModel
        """
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_if_class_attribute_exit(self):
        """Verify State class has name attribute"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_class_attribute_type_and_initials(self):
        """
        Verify 'name' attribute have correct
        data types and initial values.
        """
        state = State()
        self.assertIs(type(state.name), str)
        self.assertTrue(state.name == "")
        self.assertFalse(bool(state.name))
