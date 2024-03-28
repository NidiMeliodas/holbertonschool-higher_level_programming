#!/usr/bin/python3
"""import module"""


Rectangle = __import__('9-rectangle').Rectangle
"""Rectangle class"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)