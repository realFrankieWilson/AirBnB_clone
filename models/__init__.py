#!/usr/bin/python3
""" This module create a unique instance of FileStorage and
call reload to load existing data."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
