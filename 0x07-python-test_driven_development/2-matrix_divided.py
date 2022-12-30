#!/usr/bin/python3
"""Matrix Module

    This Module contains code for the Matrix division task on ALX
"""


def matrix_divided(matrix, div):
    """matrix_divided function

    The matrix_divided function divides all elements of a matrix
    and returns the result

    Args:
                matrix : list of list of numbers integers
                div (int): Integer or float
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not valid_matrix_type(matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not valid_matrix_size(matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result = list(
        map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))
    return result


def valid_matrix_type(matrix):
    """valid_matrix_type function

    This function validates that a matrix is a list of
    lists of integers and floats.

    Args:
        matrix : list of list containing numbers
    """

    for row in matrix:
        if not isinstance(row, list):
            return False

        for num in row:
            if not isinstance(num, float) and not isinstance(num, int):
                return False

    return True


def valid_matrix_size(matrix):
    """valid_matrix_size function

    This function validates that each row of a matrix
    has equal number of elements

    Args:
        matrix : list of list containing numbers
    """

    row_size = None

    for row in matrix:
        if row_size is None:
            row_size = len(row)
            continue

        if len(row) != row_size:
            return False

    return True
