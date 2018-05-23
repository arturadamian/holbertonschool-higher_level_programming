#!/usr/bin/python3
"""creating Rectangle class"""
from models.base import Base
"""importing Base class"""


class Rectangle(Base):
    """a new inherited class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
        width: width of the rectagle
        height: height of the rectangle
        x: x
        y: y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
        value (int): value
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Args:
        value (int): value
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y

        Args:
        value (int): value
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
        value (int): value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """calculates the area"""

        return self.__width * self.__height

    def display(self):
        """displays the rectangle"""

        print('\n' * self.y + '\n'.join(
            ' ' * self.x + ('#' * self.width) for i in range(self.height)))

    def __str__(self):
        """returns a readable string"""

        return "[Rectangle]({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute

        Args:
        args: arguments
        kwargs: key/value arguments
        """
        if args:
            i = 0
            for val in args:
                if i == 0:
                    self.id = val
                if i == 1:
                    self.width = val
                if i == 2:
                    self.height = val
                if i == 3:
                    self.x = val
                if i == 4:
                    self.y = val
                i += 1
        else:
            for key, val in kwargs.items():
                    if key == "id":
                        self.id = val
                    if key == "width":
                        self.width = val
                    if key == "height":
                        self.height = val
                    if key == "x":
                        self.x = val
                    if key == "y":
                        self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
