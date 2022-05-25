#!/usr/bin/python3
"""unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer'). max_integer

class TestMax(unittest.TestCase):
    """tests"""

    def test0(self):
        """test empty list"""
        t = []
        self.assertEqual(max_integer(t), None)

    def test1(self):
        """test list of one element"""
        t = [1]
        self.assertEqual(max_integer(t), 1)

    def test2(self):
        """test list with negatives"""
        t = [-1, -5, -13]
        self.assertEqual(max_integer(t), -1)

    def test3(self):
        """test one negative number in list"""
        t = [-1, 5, 13]
        self.assertEqual(max_integer(t), 13)

    def test4(self):
        """test max at beginning"""
        t = [15, 1, 2]
        self.assertEqual(max_integer(t), 15)

    def test5(self):
        """test max in the middle"""
        t = [1, 15, 2]
        self.assertEqual(max_integer(t), 15)

    def test 6(self):
        """test max at the end"""
        t = [1, 2, 15]
        self.assertEqual(max_integer(t), 15)

if __name__ == '__main__':
    unittest.main()
