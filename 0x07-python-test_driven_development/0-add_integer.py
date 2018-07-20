#!/usr/bin/python3
"""
add_integer - adds two integers

"""


def add_integer(a, b=98):
    """
    Args:
    a (int, float): first parameter
    b (int, float): second parameter

    Raises:

    TypeError: a must be an integer
    TypeError: a must be an integer
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
