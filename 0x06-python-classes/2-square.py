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
        self.__size = size
        try:
            size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except ValueError:
            raise TypeError("size must be an integer")
