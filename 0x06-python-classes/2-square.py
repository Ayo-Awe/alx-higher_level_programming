#!/usr/bin/python3

"""2-Square Module

This module contains a class definition for a
square

"""


class Square:
    """This class represents a square of definite size

    """

    def __init__(self, size=0):
        """Constructor for Square class

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # size of square
