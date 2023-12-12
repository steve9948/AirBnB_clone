#!/usr/bin/python3
""" The Module for serializing and deserializing python objects to/from json """

import json


class FileStorage():
    """ Serializer and deserializer class for the python objects """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ The return value as the dictionary of all objects """
        self.reload()
        return FileStorage.__objects

    def new(self, object):
        """ Sets the in __objects obj with key <obj class name>.id """
        self.reload()
        string = object.__class__.__name__ + "." + object.id
        FileStorage.__objects[string] = object.to_dict()

    def save(self):
        """ Save __objects dict to the json file """
        with open(FileStorage.__file_path, mode="w", encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)
        FileStorage.__objects = {}

    def reload(self):
        """Loads the file with the json object """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except IOError:
            pass

