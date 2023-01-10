#!/usr/bin/python3
""" Add Item Module
This module contains code for alx input output
task 7
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# Load arguments and ignore first argument
args = sys.argv[1:]


# Try to Load list from file
json_list = None
try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

# Append new args and json_list to new list
new_list = []
new_list.extend(json_list)
new_list.extend(args)

# Write new list to file
save_to_json_file(new_list, filename)
