#!/usr/bin/python3
"""
    module: User
"""
from models.base_model import BaseModel


class User(BaseModel):
    ''' defines User class '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
