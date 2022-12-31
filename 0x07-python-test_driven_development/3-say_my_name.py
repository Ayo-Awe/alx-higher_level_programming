#!/usr/bin/python3
"""Say My Name Module

    This Module contains code for the Say My Name task on ALX
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function

        The say my name function prints an introduction with the
        first_name and optionally the last_name

        Args:
                first_name (string): String representing the users first name
                last_name (string): String representing the user's'last name
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
