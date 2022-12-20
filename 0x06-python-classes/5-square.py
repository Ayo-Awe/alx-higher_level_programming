#!/usr/bin/python3

"""4-Square Module

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
        self.size = size  # size of square

    def area(self):
        """Returns current area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for private size attribute
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for private size attribute

        This helps centralize validation

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the square to stdout using #
        """

        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
