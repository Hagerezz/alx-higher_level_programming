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
        self.size = size

    def size(self):
        """return self size"""
        return self.__size

    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return self.__size**2
