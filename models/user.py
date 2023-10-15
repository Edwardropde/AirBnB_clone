#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Public class attributes:
        - email (str): empty
        - password (str): empty
        - first_name (str): empty
        - last_name (str): empty
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            args: Positional arguments passed to the constructor.
            kwargs: Keyword arguments passed to the constructor.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
