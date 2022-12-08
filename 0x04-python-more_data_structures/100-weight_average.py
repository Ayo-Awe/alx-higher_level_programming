#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted_sum = sum(map(lambda t: t[0] * t[1], my_list))
    sum_of_weights = sum(map(lambda x: x[1], my_list))

    return weighted_sum/sum_of_weights
