#!/usr/bin/python3
""" This module contains the Place class (Child-class to BaseModel) """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implement the Place class.

    Args:
        city_id(str): store city id
        user_id(str): store user id.
        name(str): name of the place.
        description(str): Description of the place.
        number_rooms(int): number of room.
        number_bathrooms(int): number of bathroom
        max_guest(int): maximum number of guest.
        price_by_night(int): price per night.
        latitude(float): Latitude of the place.
        longitude(float): Longitude of the place.
        amenity_ids(string): List of Amenity id.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
