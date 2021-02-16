#!/usr/bin/python3

"""
    class Place
"""


class Place(BaseModel):
    """ class Place """

    BaseModel.city_id = ""
    BaseModel.user_id = ""
    BaseModel.name = ""
    BaseModel.description = ""
    BaseModel.number_rooms = 0
    BaseModel.number_bathrooms = 0
    BaseModel.max_guest = 0
    BaseModel.price_by_night = 0
    BaseModel.latitude = 0.0
    BaseModel.longitude = 0.0
    BaseModel.amenity_ids = ""
