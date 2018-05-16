#!/usr/bin/python3


class BaseGeometry:
    """ class
    """
    def area(self):
        """calculates the area of a class

        Raises:
            Exception: msg
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): name
            value (int): value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherited class
    """
    def __init__(self, width, height):
        """instantiation

        Args:
            width: width
            height: height
        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """calculates the area
        """
        return self.__width * self.__height

    def __str__(self):
        """ a string
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
