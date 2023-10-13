#!/usr/bin/python3
""" This module implement the User clas (Child-class to BaseModel) """
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel class
    
    Args:
        email(str): the user's email.
        password(str): the user's password.
        first_name(str): the user's first name.
        last_name(str): the user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    