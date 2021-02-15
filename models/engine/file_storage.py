#!/usr/bin/python3

from datetime import datetime
import json

class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        self.__objects.__setitem__("{}.{}".format(obj.__class__.__name__, obj.id), obj.__dict__)

    def save(self):
#        for item in self.__objects:
#            self.__objects[item]['created_at'] = 'toto'
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            None
