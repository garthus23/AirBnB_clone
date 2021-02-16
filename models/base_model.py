#!/usr/bin/python3
""" date module, uuid and models """
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """  classe Basemodel """

    def __init__(self, *args, **kwargs):
        """ init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if (kwargs):
            for k in kwargs:
                if k is not "created_at" and k is not "__class__":
                    if k is not "updated_at":
                        self.__dict__[k] = kwargs[k]
                if k is "created_at" or k is "updated_at":
                    self.__dict__[k] =\
                        datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f')
        storage.new(self)

    def save(self):
        """ update the update attrib """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ return dict object """
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        return(self.__dict__)

    def __str__(self):
        """ str method """
        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))
