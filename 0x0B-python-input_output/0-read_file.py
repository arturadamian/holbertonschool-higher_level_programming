#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): filename
    """
    f = open(filename, "r")
    print(f.read())
