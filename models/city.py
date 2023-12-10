#!/usr/bin/python3
""" The city Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ Here, the city class contains both state ID and name """
    state_id = ""
    name = ""
