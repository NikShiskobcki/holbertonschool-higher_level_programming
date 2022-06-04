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

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square data"""
        if args and len(args) > 0:
            key = ["id", "size", "x", "y"]
            for a, b in enumerate(args):
                setattr(self, key[a], b)
        else:
            for a, b in kwargs.items():
                setattr(self, a, b)
