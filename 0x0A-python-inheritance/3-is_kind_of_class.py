#!/usr/bin/python3
"""checks the object"""


def is_kind_of_class(obj, a_class):
    """check if isinstance

    Args:
        obj: an object
        a_class: a class

    Returns: True or False
    """
    return isinstance(obj, a_class)
