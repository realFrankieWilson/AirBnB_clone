#!/usr/bin/python3
""" This module implement the Amenity class (Child-class to BaseModel) """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherit from BaseModel
    
    Args:
        name(str): name of the amenity.
    """
    name = ""