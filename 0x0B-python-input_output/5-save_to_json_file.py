#!/usr/bin/python3
""" Save To Json File Module
This module contains code for alx input output
task 5
"""

import json


def save_to_json_file(my_obj, filename):
    """ save_to_json Function
    This saves the json (serialized) representaion of my_obj
    in a json file with the specified filename
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(obj=my_obj, fp=file)
