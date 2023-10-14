#!usr/bin/python3
"""The FileStorage class"""

import datetime
import json
import os

class FileStorage:
    """Stores and retrieves data """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns a dictionary object"""
        return FileStorage.__objects


    def new(self, obj):
        """Sets objects with key <obj class name>.id"""
        formated_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[formated_key] = obj

    def save(self):
        """Serializes objects to the JSON FILE with path:__file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            my_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(my_dict, f)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
