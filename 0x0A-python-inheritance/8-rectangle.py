#!/usr/bin/python3
"""class basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class"""


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """init"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
