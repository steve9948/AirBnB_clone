#!/usr/bin/python3
""" create the instructed base model """
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
            create the base model instance
            or recreate base model instance for the dictionary
        """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        """ Defines the string representation of the object """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Updates the updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Creates custom dictionary __dict__
            (i.e. the dictionary instance attributes)
        """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        # the __class__ key is needed to recreate the object
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
