#!/usr/bin/python3
"""inherits from Module
This module contains code for task 4 of the alx
python inheritance project
"""


def inherits_from(obj, a_class):
    """inherits_from Function
    A function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class; otherwise False.

    Args:
            obj(object): object
            a_class: parent class
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
