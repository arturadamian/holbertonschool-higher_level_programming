#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file

    Args:
        filename (str): filename
        nb_lines (int): number of lines
    """
    count = 0
    with open(filename, "r") as f:
        for line in f:
            count += 1
            print(line, end="")
            if count == nb_lines:
                break
