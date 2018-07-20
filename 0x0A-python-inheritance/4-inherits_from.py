#!/usr/bin/python3
"""checks an object"""


def inherits_from(obj, a_class):
    """if is an instance of inherited class

    Args:
        obj: an object
        a_class: a class

    Returns:
        True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
