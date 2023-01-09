#!/usr/bin/python3
"""Square Module
This module contains code for task 10 of the alx
python inheritance project
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class
        Inherits from the Rectangle class
    """

    def __init__(self, size):
        """init Function
        Initialises the object instance with a size
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """area Function
        The area function returns the area of the
        square
        """
        return (self.__size ** 2)
