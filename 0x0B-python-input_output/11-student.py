#!/usr/bin/python3
""" Student Module
This module contains code for alx input output
task 11
"""


class Student:
    """ Student Class
    """

    def __init__(self, first_name, last_name, age):
        """__init__ function
        Initialises an instance of the student class
        with a first_name, last_name and an age
        """

        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.age = age  # string

    def to_json(self, attrs=None):
        """to_json function
        This is a function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an instance of a student
        """

        # Create a copy of the dictionary representation
        dic_rep = self.__dict__.copy()

        # If attrs is specified remove unwanted attributes
        if attrs is not None:
            # Create a copy of keys in object representation
            keys = list(dic_rep.keys())[:]

            # Remove unwanted attributes
            for key in keys:
                if not attrs.__contains__(key):
                    dic_rep.pop(key)

        return dic_rep

    def reload_from_json(self, json):
        """reload_from_json function
        This is a function hat replaces all attributes of the Student instance

            Args:
                json(dict)
        """
        # loop through the keys in the json and modify the object instance
        for key in json.keys():
            self.__setattr__(key, json[key])
