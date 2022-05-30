#!/usr/bin/python3
"""class basegeometry"""


Rectangle = __import__('9-rectangle').Rectangle
"""imports class"""


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
