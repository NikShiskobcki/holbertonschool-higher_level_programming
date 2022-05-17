#!/usr/bin/python3
"""defines a class square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """init size"""
        self.size = size

    def area(self):
        """current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints square to stdout"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print("")
