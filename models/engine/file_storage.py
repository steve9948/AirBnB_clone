#!/usr/bin/python3
"""
Defines the FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in obj with key."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file path."""
        save_dict = {}
        for key, obj in self.__objects.items():
            save_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(save_dict, file)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to __objects.
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(cls.__file_path, "r", encoding="utf-8") as file:
                dict_to_obj = json.load(file)
                for key, value in dict_to_obj.items():
                    class_name = value['__class__']
                    cls_to_ins = classes.get(class_name)
                    if cls_to_ins:
                        obj = cls_to_ins(**value)
                        cls.__objects[key] = obj
        except FileNotFoundError:
            pass
