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

    def area(self):
        """area function

        The area function returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter function

        The perimeter function returns the perimeter of the rectangle instance
        If either the height or width is 0, the perimeter of the rectangle is 0
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2*(self.height + self.width)

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ""

        row = "#" * self.width
        return "\n".join([row]*self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
