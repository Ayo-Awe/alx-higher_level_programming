#!/usr/bin/python3
"""base geometry Module
This module contains code for task 7 of the alx
python inheritance project
"""


class BaseGeometry:
    """BaseGeometry Class
        Instance Methods:
            area(public)
    """

    def area(self):
        """area Function
        The area function simply raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validation Function
        This function validates value
            Args:
            name(string): is always a string
            value(int): integer greater than zero
        """

        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
