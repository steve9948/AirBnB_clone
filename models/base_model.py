#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Creating an instance'''

    def __init__(self, *args, **kwargs):
        '''
        Initialize a new instance of the BaseModel class.
        *args, **kwargs arguments for the constructor of a BaseModel
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''Returns a string representation of the BaseModel instance.'''
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        '''Updates updated_at with the current datetime.'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''
        result_dict = dict(self.__dict__)
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
