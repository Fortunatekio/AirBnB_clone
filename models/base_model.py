#!/usr/bin/python3
""" this is the 'BaseMode'class"""
#from .storage import Storage
from uuid import uuid4
from datetime import datetime

    #storage = Storage()

class BaseModel:
    """
    Serves as the base class for all our classes
    Attributes:
        id: A unique Id for every instance of the class
        created_at: contains time an oject is created
        updated at: contains the timestamp when an object was updated
    methods:
        z
    """
    def __init__(self, *args, **kwargs):
        self.id = id = str(uuid4())
        self.created_at = datetime.today() 
        self.updated_at = datetime.today()
        """
         if there are keyword arrguments, check for specific keywords, 
         if found, convert their attributes to datetime objects

        """

        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """ Returns the string representation of the class instances """
        #class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self) -> None:
        """updates 'updated_at' with the current datetime when called"""
        from models import storage
        self.updated_at = datetime.today()
        storage.new(self)
        storage.save()

            #models.storage.save()

    def to_dict(self):
        """Returns a dict containing all attributes of the object;
        classname, created_at and updated_at in ISO format
        TIP: used 'self.__dict__' to return only the set instance attributes
        Returns a dict containing all keys/values
        """
        dict_repr = self.__dict__.copy()
        #dict_repr["__class__"] = type(self).__module__ + '.' + type(self).__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr

