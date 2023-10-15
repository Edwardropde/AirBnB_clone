#!/usr/bin/python3


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class represents a state in the system.

    Attributes:
        name (str): The name of the state (default is an empty string).
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
