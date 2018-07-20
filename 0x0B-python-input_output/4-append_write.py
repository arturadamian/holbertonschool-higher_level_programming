#!/usr/bin/python3


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename (str): filename
        text (str): text
    """
    with open(filename, "a") as f:
        count = f.write(text)
    return count
