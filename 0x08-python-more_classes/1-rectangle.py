#!/usr/bin/python3
""" Rectangle Class Module

This module contains a class definition for a rectangle
"""


class Rectangle:
    """ Rectangle Class

    This is definition for an empty rectangle class
    """

    def __init__(self, width=0, height=0):
        """constructor function for Rectangle object

            Args:
                width(int): width of rectangle
                height(int): height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for private property, width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private property, width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter function for private property, height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private property, height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value