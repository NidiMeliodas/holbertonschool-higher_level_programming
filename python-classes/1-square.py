#!/usr/bin/python3
'''defines a class with a private instance attribute :size'''


class Square:
    '''Class : Square with a private instance attribut'''
    def __init__(self, size):
        '''initalize square using pirvate attribute size as args'''
        self._size = size
