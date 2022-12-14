#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max = None

    for key in a_dictionary.keys():
        if max is None:
            max = key
        elif a_dictionary[key] > a_dictionary[max]:
            max = key

    return max
