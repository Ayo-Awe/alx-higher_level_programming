#!/usr/bin/python3
""" To JSON String Module
This module contains code for alx input output
task 3
"""

import json


def to_json_string(my_obj):
    """ to_json_string Function
    This function returns a serialized representation
    of my_obj
    """
    return json.dumps(my_obj)
