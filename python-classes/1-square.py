#!/usr/bin/python3
'''defines a class with a private instance attribute :size'''


class Square:
    '''A class to reprensent a square '''

    def __init__(self, size=0):
        '''Initializes a Square instance'''
        self.__size = size
