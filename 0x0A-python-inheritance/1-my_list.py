#!/usr/bin/python3
"""My List Module
This module contains code for task 1 of the alx
python inheritance project
"""


class MyList(list):
    """MyList Class
        Inherits from list
    """

    def print_sorted(self):
        """print_sorted Function
        Prints a python list but sorted in ascending order
        """
        # Create a copy of the list
        copy = self.copy()

        # Sort the copy of the list
        copy.sort()

        print(copy)
