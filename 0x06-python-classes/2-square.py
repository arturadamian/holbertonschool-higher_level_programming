#!/usr/bin/python3
class Square:
    """defines Square"""
    def __init__(self, size=0):
        """the instance of Square
        Args:
        size (int): size of the Square
        Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
