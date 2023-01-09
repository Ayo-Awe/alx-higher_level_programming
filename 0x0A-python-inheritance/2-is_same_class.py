#!/usr/bin/python3
"""Is Same Class Module
This module contains code for task 2 of the alx
python inheritance project
"""


def is_same_class(obj, a_class):
    """is_same_class Function
    This function returns true if obj is an instance
    of a_class

        Args:
            obj(object): object
            a_class: parent class
    """
    return isinstance(obj, a_class)
