#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) >= ord('a'):
            new_str += chr(ord(c) + ord('A') - ord('a'))
        else:
            new_str += c
    print("{}".format(new_str))
