#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for storing city information.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.

    Public Class Attributes:
        state_id (str): An empty string for the state ID.
        name (str): An empty string for the city name.
    """

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
