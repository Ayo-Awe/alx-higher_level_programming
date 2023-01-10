#!/usr/bin/python3
""" Class To Json Module
This module contains code for alx input output
task 8
"""


def class_to_json(obj):
    """ class_to_json Function
    This is a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """

    return obj.__dict__
