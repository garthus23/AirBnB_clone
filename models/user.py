#!/usr/bin/python3
""" parent classe """
from models.base_model import BaseModel

"""
    user class very class
"""


class User(BaseModel):
    """ user international class """
    def __init__(self):
        """ init """
        BaseModel.__init__(self)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """ strrrrrrrrrr """
        return("[User] ({}) {}".format(self.id, self.__dict__))
