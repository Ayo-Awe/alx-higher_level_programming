#!/usr/bin/python3

"""4-Square Module

This module contains a class definition for a
square

"""


class Square:
    """This class represents a square of definite size

    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for Square class

        Args:
            size (int): size of square
        """
        self.size = size  # size of square
        self.position = position

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

    @property
    def position(self):
        """Getter for private attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for private position attribute
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square to stdout using #
        """

        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            # print spaces for x coordinate
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def area(self):
        """Returns current area of the square
        """
        return self.__size ** 2
