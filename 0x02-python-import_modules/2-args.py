#!/usr/bin/python3
from sys import argv

# ignore first argument
args = argv[1:]

if __name__ == "__main__":
    if len(args) == 0:
        # No argument was passed
        print("0 arguments.")
    elif len(args) == 1:
        # exactly one argument was passed
        print("1 argument:")
    else:
        print("{} arguments:".format(len(args)))

    for index, arg in enumerate(args):
        print("{}: {}".format(index + 1, arg))
