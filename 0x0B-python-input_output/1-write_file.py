#!/usr/bin/python3
""" Write File Module
This module contains code for alx input output
task 1
"""


def write_file(filename="", text=""):
    """write_file Function
    This function writes text to a file. If the file
    doesn't exist, the file is created
    """
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written
