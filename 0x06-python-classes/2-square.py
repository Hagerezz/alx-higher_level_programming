#!/usr/bin/python3
"""Represents a square"""


class Square:
    """Represents a square"""
    pass

    def __init__(self, size=0):
        """
        new square
        Args:
            size (int) : size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """return area of square"""
        return self.__size**2
