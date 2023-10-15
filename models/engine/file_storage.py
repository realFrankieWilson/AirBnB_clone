#!/usr/bin/python3
"""
Contains the FileStorage class model

"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": User,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
<<<<<<< HEAD
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            pass
=======
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
            my_obj = json.load(f)
            my_obj = {
                k: FileStorage.classes[v['__class__']](**v)
                for k, v in my_obj.items()
                }
            FileStorage.__objects = my_obj
        # try:
        #     with open(self.__file_path, encoding="utf-8") as f:
        #         for obj in json.load(f).values():
        #             self.new(eval(obj["__class__"])(**obj))
        # except FileNotFoundError:
        #     return
>>>>>>> more_classes
