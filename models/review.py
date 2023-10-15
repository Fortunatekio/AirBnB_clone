#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits attributes and
    methods of the basemodel class with
    specified public attributes which are
    place id, user id, text.
    """
    place_id = ""
    user_id = ""
    text = ""
