#!/usr/bin/python3
"""represent a code"""
def add_integer(a, b=98):
    """
    add number
    a (int or float) : first number
    b (int or float) : second number
    """

    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return a + b
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
