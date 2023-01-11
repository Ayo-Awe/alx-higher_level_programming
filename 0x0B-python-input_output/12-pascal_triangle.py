#!/usr/bin/python3
"""Pascal Triangle Module
"""


def pascal_triangle(n):
    """pascal_triangle function
    This function returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    # P(n > 0) has at least [1] in the array
    result = [[1]]

    # Loop from 2 to n
    for i in range(1, n):
        result.append(generate_pascal_row(result[i-1]))

    return result


def generate_pascal_row(row):
    """ generate_pascal_row function
    This function returns the row succeed the
    current row in the pascal triangle sequence
    """
    result = [1]

    # Generate succeed row
    for i in range(len(row)):

        if i < len(row) - 1:
            # Add current element with adjacent neighbour
            result.append(row[i] + row[i+1])
        else:
            # Last element has no adjacent neighbour
            result.append(row[i])

    return result
