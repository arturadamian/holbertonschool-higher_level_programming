#!/usr/bin/python3
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str (str): object

    Returns:
        an object
    """
    return json.loads(my_str)
