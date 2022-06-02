#!/usr/bin/python3
"""function"""
from .base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """validates value"""
        if name == "x" or name == "y":
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """"y setter"""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns data of rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        """updates attributes"""
        le = len(args) - 1
        self.id = args[0]
        if le >= 1:
            self.width = args[1]
        if le >= 2:
            self.height = args[2]
        if le >= 3:
            self.x = args[3]
        if le >= 4:
            self.y = args[4]
