#!/usr/bin/python3
"""
This module contains a function to check if an object is an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """is_same_class function"""
    return type(obj) is a_class
