#!/usr/bin/python3
"""
The Base Module for AirBnB Console
"""
from unittest import result
import uuid
from datetime import datetime


class BaseModel:
    """The Base class"""

    def __init__(self):
        """
        instatiates an object with it's
        attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        result['__class__'] = self.__class__.__name__
        return result
