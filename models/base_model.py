#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""

# modules importation.
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """

<<<<<<< HEAD
        if kwargs:
            # stores the datetime format
            datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                        kwargs['created_at'], datetime_format
                        )
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], datetime_format
                        )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
=======
        from models import storage
        if not kwargs:
>>>>>>> 33e435d2e39820fb45deaf5e94cef6b47a302d6f
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
<<<<<<< HEAD
        """ Returns a string representation of the instance. """
        return '[{}] ({}) {}'.format(self.__class__.__name__,self.id, self.__dict__)
=======
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
>>>>>>> 33e435d2e39820fb45deaf5e94cef6b47a302d6f

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
<<<<<<< HEAD
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
                by using self._dict_, only instance attributes
                set will be returned.
                a key _class_ must be added to this dictionary
                with the class name of the object.
                created_at and updated_at must be converted
                to string object in ISO format.
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
=======
        returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
>>>>>>> 33e435d2e39820fb45deaf5e94cef6b47a302d6f
