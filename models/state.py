#!/usr/bin/python3
"""state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class that inherits from Basemodel
    public attributes name that is a string
    """

    name = ""
