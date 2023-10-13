#!/usr/bin/python3

""" This module contains all the test cases for the FileStorage class methods."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_new_and_all(self):
        model_instance = BaseModel()
        model_instance.id = "123"
        self.storage.new(model_instance)
        objects = self.storage.all()
        key = "{} {}".format(model_instance.__class__.__name__, model_instance.id)
        self.assertIn(key, objects)
        self.assertIs(objects[key], model_instance)

    def test_save_and_reload(self):
        model_instance = BaseModel()
        model_instance.id = "123"
        self.storage.new(model_instance)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()

        key = "{} {}".format(model_instance.__class__.__name__, model_instance.id)
        self.assertIn(key, objects)
        reloaded_instance = objects[key]
        self.assertEqual(reloaded_instance.id, model_instance.id)

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

if __name__ == '__main__':
    unittest.main()
