#!/usr/bin/python3
""" uuid generator module and datetime"""
import uuid
from datetime import datetime

""""
    class BaseModel
"""


class BaseModel():
    """  classe Basemodel """

    def __init__(self, *args, **kwargs):
        """ init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ update the update attrib """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return dict object """
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        return(self.__dict__)

    def __str__(self):
        """ str method """
        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))
