#!/usr/bin/python3
""" This module contain a class FileStorage that serializes
    instances to a JSON file and deserializes JSON file to instances."""
import json


class FileStorage:
    """ Serializes intances to a JSON file and
    deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Retrieve all objects from the objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new object to the objects dictionary"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Save objects to a JSON file."""
        serialized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serialized_obj[key] = obj.to_dict()

        # open the file and write the serialized objects in JSON format.
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """Load objects from JSON file."""
        try:
            # try to open the JSON file for reading.
            with open(FileStorage.__file_path, 'r') as f:
                # Load JSON data from the file.
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    obj_dict = value
                    cls = eval(cls_name)
                    # convert class name back to a class.
                    obj = cls(**obj_dict)
                    # Recreate the object.
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
