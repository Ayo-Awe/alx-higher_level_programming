#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("")
        for idx, item in enumerate(row):
            if idx != len(row) - 1:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item))
