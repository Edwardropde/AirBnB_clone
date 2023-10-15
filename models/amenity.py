#!/usr/bin/python3


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents amenities for accommodations.

    Attributes:
        name (str): The name of the amenity.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Return a string representation of the Amenity instance"""
        return "[Amenity] ({}) {}".format(self.id, self.name)
