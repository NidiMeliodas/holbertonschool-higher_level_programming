#!/usr/bin/python3
'''defines a class with a private instance attribute :size'''


class Square:
    '''A class to reprensent a square '''

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
