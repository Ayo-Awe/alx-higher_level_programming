#!/usr/bin/python3
""" Student Module
This module contains code for alx input output
task 9
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

    def to_json(self):
        """to_json function
        This is a function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an instance of a student
        """

        return self.__dict__
