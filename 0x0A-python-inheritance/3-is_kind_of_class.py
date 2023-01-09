#!/usr/bin/python3
"""is_kind_of_class
This module contains code for task 3 of the alx
python inheritance project
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class Function
    This function returns true if an object (obj) is
    derived from another parent class or is of the
    same class

    Args:
            obj(object): object
            a_class: parent class
    """
    return isinstance(obj, a_class)
