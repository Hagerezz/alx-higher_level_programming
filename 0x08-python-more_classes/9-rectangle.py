#!/usr/bin/python3
"""Represents a rectangle"""


class Rectangle:
    """
    Represents a rectangle
    Attributes:
        number_of_instances (int): number of Rectangle instances.
        print_symbol (any): symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize rectangle
        Args:
            width (int) : width
            height (int) : height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return self width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return self height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """return printable"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * self.width]
                             * self.height)

    def __repr__(self):
        """return string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
