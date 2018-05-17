#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): filename
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
    f.closed
