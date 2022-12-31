#!/usr/bin/python3
"""Print Square Module

    This Module contains code for the Print Square task at ALX
"""


def print_square(size):
    """print_square function

        The print_square function prints out a square to
        stdout using the # symbol

        Args:
                size (int): Integer representing the size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
