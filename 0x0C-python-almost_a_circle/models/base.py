#!/usr/bin/python3

""" Base Module
"""


class Base:
    """Base Class
    The base class is the base of
    all other classes in this project


    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        Initialises the instance with 'id' if provided
        or it defaults to the number of objects instantiated
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
