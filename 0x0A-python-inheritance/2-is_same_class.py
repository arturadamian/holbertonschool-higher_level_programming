#!/usr/bin/python3
"""checks if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """checks the object

    Args:
        obj: an object
        a_class: specified class

    Returns: True or False
    """
    return type(obj) == a_class
