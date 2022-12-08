#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def handler(element): return replace if element == search else element
    return list(map(handler, my_list))
