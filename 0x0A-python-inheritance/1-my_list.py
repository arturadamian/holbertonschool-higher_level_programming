#!/usr/bin/python3
"""writing a class MyList that inherits from a list"""


class MyList(list):
    """iheritance

    Args:
        list: list
    """

    def print_sorted(self):
        """prints the sorted inherited list
        """
        print(sorted(self))
