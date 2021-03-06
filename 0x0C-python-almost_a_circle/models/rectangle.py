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

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """"y setter"""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """areaaaaaaaaaaaaaaaaaaaaa"""
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

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args and len(args) > 0:
            key = ["id", "width", "height", "x", "y"]
            for a, b in enumerate(args):
                setattr(self, key[a], b)
        else:
            for a, b in kwargs.items():
                setattr(self, a, b)

    def to_dictionary(self):
        """returns dictionary"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
