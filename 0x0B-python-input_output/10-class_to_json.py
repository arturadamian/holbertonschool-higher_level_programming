#!/usr/bin/python3


def class_to_json(obj):
    """returns the dictionary description with simple data structure

    Args:
        obj: object

    Returns:
        dict: the dictionary description
    """
    return obj.__dict__
