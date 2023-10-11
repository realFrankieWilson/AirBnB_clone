#!/usr/bin/python3
# base_model.py

# modules importation.
from uuid import uuid4
from datetime import datetime

class BaseModel():
	"""Defines all common attributes/methods for other classes."""

	def __init__(self, id=''):
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		return '{[]} {()} {}'.format(BaseModel.__name__, self.id, self.__dict__)

	def save(self):




my_obj = BaseModel(123, 
print(my_obj.id)
