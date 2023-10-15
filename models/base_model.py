#!/usr/bin/python3
"""Difines The BaseModel Class"""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier for each BaseModel instance.
        created_at (datetime): The datetime when the instance is created
        updated_at (datetime): The datetime when the instance is last updated

    Methods:
        __init__(): Initializes a new BaseModel with unique ID and datetimes.
        __str__(): Returns a string representation of the BaseModel instance.
        save(): Updates the 'updated_at' attribute with the current datetime.
        to_dict(): Returns dictionary representation of BaseModel instance.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        orm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, orm)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
    
    def save(self, storage):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
