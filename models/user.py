#!/usr/bin/python3
"""creation of python class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class that inherits from BaseModel
    with public attributes , which are email, password
    first name and last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
