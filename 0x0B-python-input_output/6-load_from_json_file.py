#!/usr/bin/python3
""" Load From Json File Module
This module contains code for alx input output
task 6
"""

import json


def load_from_json_file(filename):
    """ load_from_json Function
    This function that creates an object from
    a json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        my_obj = json.load(fp=file)
        return my_obj
