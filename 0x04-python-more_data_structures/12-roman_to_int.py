#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) and not None:
        return 0

    numerals = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    previous_token = None

    for token in roman_string[::-1]:
        if previous_token is None:
            num += numerals[token]
            previous_token = token
        else:
            # Subtraction notation
            if (numerals[previous_token] > numerals[token]):
                # Subtract value
                num -= numerals[token]
            else:
                # Regular notation
                num += numerals[token]
            previous_token = token

    return num
