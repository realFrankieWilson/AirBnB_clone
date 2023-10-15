#!/usr/bin/python3
""" This module contains the Review class (Child-class to BaseModel) """
from models.base_model import BaseModel


class Review (BaseModel):
    """
    Implement the Review module

    Args:
       place_id(str): place id.
       user_id(str): user id.
       test(str): user review.
    """
    place_id = ""
    user_id = ""
    text = ""
