#!/usr/bin/python3
"""defines a class square"""


class Square:
    """class square"""

    def __init__(self, size=0, position=(0, 0))):
        """init class"""
        self.size = size
        self.position = position

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


    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if ((type(value) is not tuple) or
                (len(value) != 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int) or
                (value[0] < 0) or
                (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value



    def my_print(self):
        """prints square to stdout"""
        if self.size == 0:
            print("")
        else:
            for x in range(self.position[1]):
                print("")
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for n in range(self.size):
                    print("#", end="")
                print("")
