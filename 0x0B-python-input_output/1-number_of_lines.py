#!usr/bin/python3


def number_of_lines(filename=""):
    """returns the number of lines

    Args:
        filename (str): filenme
    """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count
