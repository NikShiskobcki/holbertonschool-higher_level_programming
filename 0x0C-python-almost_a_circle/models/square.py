#!/usr/bin/python3
"""function"""
from .rectangle import Rectangle


class Square(Rectangle):
    """rectangle square"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints square data"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))
