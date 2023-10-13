#!/usr/bin/python3
""" This module implement the State class (Child-class to BaseModel) """
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherit from BaseModel

    Args:
        name(str): name of state
    """
    name = ""
