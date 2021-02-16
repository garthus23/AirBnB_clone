#!/usr/bin/python3
"""module datetime and json"""
from datetime import datetime
import json

"""
    class FileStorage
"""


class FileStorage():
    """ class filestorage """
    def __init__(self):
        """ init function """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ all method """
        return(self.__objects)

    def new(self, obj):
        """ new method """
        self.__objects.__setitem__(
            "{}.{}".format(obj.__class__.__name__,
                           obj.id),
            obj.__dict__)

    def save(self):
        """ save method """
#        for item in self.__objects:
#            self.__objects[item]['created_at'] = 'toto'
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        """ reload method """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            None
