#!/usr/bin/python3
from sys import argv

# exclude the first argument
args = argv[1:]

if __name__ == "__main__":
    if len(args) == 0:
        print("0")
    else:
        # cast all elements and sum them
        sum = sum([int(arg) for arg in args])
        print("{}".format(sum))
