#!/usr/bin/python3
""" Rectangle Class Module

This module contains a class definition for a rectangle
"""


class Rectangle:
    """ Rectangle Class

    This is definition for an empty rectangle class

        Class Attributes:
            number_of_instances(int): number of rectangle instances
            print_symbol(any): symbol used to print rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal

        Returns the biggest of two rectangle objects.
        If both rectangles are equal then rect_1 is returned
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """square function

        The square function is a factory function that returns a new
        instance of a rectangle where the width == height == size
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """constructor function for Rectangle object

            Args:
                width(int): width of rectangle
                height(int): height of rectangle
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """__str__
        returns the square in using the specified print_symbol.
        By default print_symbol is #.
        If either the width or height is 0, an empty string is returned
        """
        if (self.width == 0 or self.height == 0):
            return ""

        row = f"{self.print_symbol}" * self.width
        return "\n".join([row]*self.height)

    def __repr__(self):
        """__repr__
        Returns a representation of the object that would return a new
        instance of a rectangle if passed into the eval function
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """__del__
        Prints a message before deleting an instance of the Rectangle class and
        decrements the number of instances
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
