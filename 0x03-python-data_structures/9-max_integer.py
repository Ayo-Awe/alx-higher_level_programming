#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]

    for num in my_list:
        max = num if num > max else max

    return max
