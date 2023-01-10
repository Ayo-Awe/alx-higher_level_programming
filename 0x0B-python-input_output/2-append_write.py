#!/usr/bin/python3
""" Append Write Module
This module contains code for alx input output
task 2
"""


def append_write(filename="", text=""):
    """append_write Function
    This function appends texts to the end of a file. If the file
    doesn't exist, the file is created
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written
