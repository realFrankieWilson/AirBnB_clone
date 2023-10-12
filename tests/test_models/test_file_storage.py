#!/usr/bin/python3

""" This module contains all the test cases for the FileStorage class."""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the test class.
        """
        cls.storage = FileStorage()
        cls.obj = BaseModel()
        cls.obj.save()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after the test class.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")


    def test_all(self):
        """
        Test the all() method of FileStorage.
        """
        objects = self.storage.all()
        self.assertTrue(isinstance(objects, dict))
        self.assertIn("BaseModel.{}".format(self.obj.id), objects)

    def test_new(self):
        """
        Test the new() method of FileStorage.
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), objects)

    def test_save(self):
        """
        Test the save() method of FileStorage.
        """
        new_obj = BaseModel()
        new_obj.save()
        objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), objects)

    def test_reload(self):
        """
        Test the reload() method of FileStorage.
        """
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn("BaseModel.{}".format(self.obj.id), objects)


if __name__ == '__main__':
    unittest.main()
