#!/usr/bin/python3
"""
matrix_divided - divids list of lists
"""


def matrix_divided(matrix, div):
    """
    Args:

    matrix (list of lists): first parameter
    div (int, float): second parameter

    Raises:

    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: div must be a number
    TypeError: Each row of the matrix must have the same size
    ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list) or not any(isinstance(y, list)
                                               for y in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(isinstance(x, (float, int))for y in matrix for x in y):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if not all(len(x) == len(next(iter(matrix))) for x in iter(matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in y] for y in matrix]
