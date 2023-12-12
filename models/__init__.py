#!/usr/bin/python3
"""
    Creating a unique FileStorage instanc for the client
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
