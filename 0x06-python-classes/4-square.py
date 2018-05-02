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

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size
        Args:
        value (int): size of the Square
        Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
