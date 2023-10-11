#!/usr/bin/python3
""" this is the 'BaseMode'class"""
from uuid import uuid4
from datetime import datetime
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
        self.update_at = datetime.today()
        """
         if there are keyword arrguments, check for specific keywords, 
         if found, convert their attributes to datetime objects

        """

        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S.%f")
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%d %H:%M:%S.%f")

        for key, value in kwargs.items():
            setattr(self, key, value)

        def __str__(self):
            """ Returns the string representation of the class instances """
            cls = self.__class__.__name__
            return "[{}] ({}) ({})".format(self.cls, self.created_at, self.__dict__)

        def save(self):
            """updates 'update_at' with the current datetime when called"""
            self.update_at = datetime.now()


        def to_dict(self):
            """Returns a dict containing all attributes of the object;
                classname, created_at and updated_at in ISO format
                TIP: used 'self.__dict__' to return only the set instance attributes
            """
            """Returns a dict containing all keys/values"""
            dict = self.__dict__.copy()
            dict["__class__"] = self.__class__.__name__
            dict["created_at"] = dict["created_at"].isoformat()
            dict["updated_at"] = dict["updated_at"].isoformat()
            return dict

class MyModel(BaseModel):
    def save(self):
        pass
kwargs = {
        "name": "My First Model",
        "my_number": 89,
        }

my_model = BaseModel(**kwargs)

for key, value in my_model.__dict__.items():
    print("{}: {}".format(key, value))
print(my_model)
