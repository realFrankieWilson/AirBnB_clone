import unittest
from models.base_model import BaseModel

""" This module contains the test cases for BaseModel class
    methods. """


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class in the models/base_model module."""

    def test_str_representation(self):
        """ Test the string representation of the object."""
        obj = BaseModel()
        string_repr = str(obj)
        self.assertIn("[BaseModel]", string_repr)
        # check if class name is present.
        self.assertTrue(hasattr(obj, 'id'))
        # check is 'id' attribute is present.
        self.assertTrue(hasattr(obj, 'created_at'))
        # check is 'created_at' attribute is present
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save_method(self):
        """ Test that the save method updates the 'updated_at' attribute."""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save
        self.assertNotEqual(prev_updated_at, obj.updated_at)
        # check if 'updated_at' was updated.

    def test_to_dict_method(self):
        """ Test that the to_dict method returns a valid dictionary
        representation of the object."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        # check if '__class__' is set correctly.
        self.assertTrue(hasattr(obj_dict, 'id'))
        # check if 'id' attribute is present.
        self.assertTrue(hasattr(obj_dict, 'created_at'))
        # check if 'created_at' attribute is present.
        self.assertTrue(hasattr(obj_dict, 'updated_at'))
        # check is 'updated_at attribute is present.


if __name__ == '__main':
    unittest.main()
