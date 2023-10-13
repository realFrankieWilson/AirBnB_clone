#!/usr/bin/python3
""" This module contains the City class (Child-class to BaseModel) """
from models.base_model import BaseModel


class City(BaseModel):
    """
    Implement the City class.

    Args:
        state_id(str): Store the state_id.
        name(str): name of state.

    """
    state_id = ""
    name = ""
