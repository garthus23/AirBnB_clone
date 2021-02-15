#!/usr/bin/python3

import json

class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        __objects.__setitem__(obj, self.id)

    def save(self):
        with open(__file_path, 'w') as f:
            f.write(json.dumps(__objects))
