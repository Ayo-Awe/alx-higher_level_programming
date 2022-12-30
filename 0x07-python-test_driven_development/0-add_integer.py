#!/usr/bin/python3
"""Add Integer Module

    This Module contains code for the add integer task on ALX
"""


def add_integer(a, b=98):
    """add_integer function

    The add_integer function adds two integers together
    and returns the result

    Args:
                a (int): Integer or float
                b (int): Integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
