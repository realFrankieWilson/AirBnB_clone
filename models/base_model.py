#!/usr/bin/python3
# base_model.py

# modules importation.
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """ Initialize a new instance of the BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a string representation of the instance. """
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """"Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
                by using self.__dict__, only instance attributes
                set will be returned.
                a key __class__ must be added to this dictionary
                with the class name of the object.
                created_at and updated_at must be converted
                to string object in ISO format.
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
