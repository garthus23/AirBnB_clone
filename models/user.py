#!/usr/bin/python3
""" parent classe """
from models.base_model import BaseModel

"""
    user class very class
"""


class User(BaseModel):
    """ user international class """

    BaseModel.email = ""
    BaseModel.password = ""
    BaseModel.first_name = ""
    BaseModel.last_name = ""

    def __init__(self):
        """ init """
        BaseModel.__init__(self)
    
    def __str__(self):
        """ strrrrrrrrrr """
        return("[User] ({}) {}".format(self.id, self.__dict__))
