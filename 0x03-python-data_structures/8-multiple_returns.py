#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    first_char = None if sentence == ""else sentence[0]

    return (lenght, first_char)
