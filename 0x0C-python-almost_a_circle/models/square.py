#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    The square class inherits from rectangle as
    it is a rectangle with height = width
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor function"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update function
        Updates square attributes in the order
        id, size, x, y
        keyword args are also allowed
        """
        # List of instance attributes in the order they are passed as *args
        attr_keys = ["id", "size", "x", "y"]

        # Set attributes based on the no keyword args
        for index, arg in enumerate(args):
            self.__setattr__(attr_keys[index], arg)

        # If args is not empty, skip kwargs
        if len(args) != 0:
            return

        for key, value in kwargs.items():
            if key in attr_keys:
                self.__setattr__(key, value)

    def to_dictionary(self):
        """to_dictionary function
        Converts square instance to a
        dictionary representation of the instance
        """
        # Attribute keys
        attr_keys = ["id", "size", "x", "y"]

        # Define new dictionary and assign keys with the corresponding values
        dic = {}

        for key in attr_keys:
            dic[key] = self.__getattribute__(key)

        return dic
