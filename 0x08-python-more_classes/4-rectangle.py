#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """prints rectangle"""
        rtg = ""
        if self.height == 0 or self.width == 0:
            return rtg
        else:
            for i in range(self.height):
                for n in range(self.width):
                    rtg += "#"
                if (i != self.height - 1):
                    rtg += "\n"
            return rtg
    def __repr__(self):
        """prints representation"""
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")
