#!/usr/bin/python3
"""Rectangle Module
This module contains code for task 8 of the alx
python inheritance project
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class
        Inherits from the BaseGeometry class
    """

    def __init__(self, width, height):
        """init Function
        Initialises the object instance with a width and
        height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
