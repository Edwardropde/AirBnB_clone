#!/usr/bin/python3

import uuid
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
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Current datetime
            self.updated_at = self.created_at  # Initial val same tocreate_at

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self, storage):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()  # Get a copy of instance's attributes
        obj_dict['__class__'] = self.__class__.__name__  # Add the class name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
