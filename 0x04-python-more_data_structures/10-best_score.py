#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    max = 0

    for key in a_dictionary.keys():
        if a_dictionary[key] > max:
            max = a_dictionary[key]

    return max
