#!/usr/bin/python3
"""this is the class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class definition for a city. the city
    class has two attributes , state id and name
    """
    state_id = ""
    name = ""
