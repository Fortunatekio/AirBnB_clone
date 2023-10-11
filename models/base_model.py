#!/usr/bin/python3
""" this is the 'BaseMode'class"""
from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = id = str(uuid4())
        self.created_at = datetime.today() 
        self.update_at = datetime.today()

        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S.%f")
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%d %H:%M:%S.%f")

        for key, value in kwargs.items():
            setattr(self, key, value)

        def __str__(self):
            """ Returns the string representation of the class instances """
            cls = __class__.__name__
            return "[{}] ({}) ({})".format(self.cls, self.created_at, self.__dict__)
        def save(self):
            """updates 'update_at' with the current datetime"""
            self.update_at = datetime.today()
            models.storage.new(self)
        def to_dict(self):
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

print(my_model)

