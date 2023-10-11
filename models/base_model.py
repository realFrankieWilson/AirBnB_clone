#!/usr/bin/python3
# base_model.py

# modules importation.
from uuid import uuid4
from datetime import datetime

class BaseModel():
	"""Defines all common attributes/methods for other classes."""

	def __init__(self, id=''):
		""" Initialize a new instance of the BaseModel """
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		""" Return a string representation of the class instance. """
		return '{[]} {()} {}'.format(self.__class__.__name__, self.id, self.__dict__)
	
	def save(self):
		""""Update the updated_at attribute with the current datetime."""
		self.updated_at = datetime.now()