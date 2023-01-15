#!/usr/bin/python3

""" Base Module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function

        Converts list of dictionaries to a json string
        """

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Writes the json string representation of a
        list of objects to a file
        """
        dict_objs = None

        if list_objs is not None:
            dict_objs = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dict_objs))
            file.close()

    @staticmethod
    def from_json_string(json_string):
        """from_json_string function

        Converts json string to dictionary
        """

        # Validation
        if json_string is None or json_string == "":
            return []

        # Parse json string to dictionary
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create function

        Converts a dictionary to an instance of the
        class
        """
        # Set dummy values that are valid for both square and rectangle
        instance = cls(2, 3)

        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """load_from_file function

        Returns a list of instances of cls
        from the json file with the class filename. If file doesn't
        exist, an empty list is returned
        """

        try:
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as file:
                m_dicts = cls.from_json_string(file.read())
                instances = [cls.create(**m_dict) for m_dict in m_dicts]
                return instances

        except FileNotFoundError:
            return []
