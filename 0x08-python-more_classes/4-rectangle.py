#!/usr/bin/python3
class Rectangle:
    """ a new class"""

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
        width (int): width of Rectangle
        height (int): height of Rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getting width

        Returns:
        int: weight
        """
        return self.__width

    @property
    def height(self):
        """getting height

        Returns:
        int: height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """setting width

        Args:
        width (int): width

        Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0

        """
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setting height

        Args:
        height (int): height

        Raises:
        TypeError: height must be an integer
        ValueError: height must be >= 0

        """
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the area of Rectangle

        Returns:
        int: area
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter

        Returns:
        int: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints the area with '#"

        Returns:
        str: a string of # or an empty one

        """
        area = ""
        if self.__width == 0 or self.__height == 0:
            return area
        return '\n'.join(('#' * self.__width) for i in range(self.__height))

    def __repr__(self):
        """returns a string representation

        Returns:
        str: returns a string representation of the rectangle
        to be able to recreate a new instance
        """
        return ('Rectangle({},{})'.format(self.__width, self.__height))
