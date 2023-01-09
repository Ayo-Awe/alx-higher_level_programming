#!/usr/bin/python3

""" This module contains code for the lookup task
in alx higher level programming.
"""


def lookup(obj):
    """Lookup Function
    The lookup function returns a list containing all the available attributes
    and methods available for an object

                Args:
                        obj(object): any valid python object
    """
    attributes = dir(obj)
    return list(attributes)
