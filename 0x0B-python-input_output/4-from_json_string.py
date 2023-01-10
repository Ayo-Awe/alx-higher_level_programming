#!/usr/bin/python3
""" From JSON String Module
This module contains code for alx input output
task 4
"""

import json


def from_json_string(my_str):
    """ from_json_string Function
    This function returns a deserialized representation
    of a json string, my_str
    """
    return json.loads(my_str)
