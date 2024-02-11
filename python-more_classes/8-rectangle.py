#!/usr/bin/python3
"""This is a module for a rectangle class."""


class Rectangle():
    """This is a class for a rectangle object."""
    pass

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join((str(self.print_symbol) * self.width
                          for worst_than_square in range(self.height)))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
