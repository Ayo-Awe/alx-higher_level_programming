#!/usr/bin/python3
""" Read File Module
This module contains code for alx input output
task 0
"""


def read_file(filename=""):
    """read_file function
    The read file function prints all the lines in a
    text file
    """
    # Open file
    with open(filename, "r", encoding="utf-8") as f:
        # Print each line
        for line in f.readlines():
            print(line, end="")
