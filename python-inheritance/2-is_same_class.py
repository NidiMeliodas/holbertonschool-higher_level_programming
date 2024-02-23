#!/usr/bin/python3
"""
This module contains a function to check if an object is an instance
of a specified class.
"""


def is_same_class(obj, a_class):
	"""Check if an object is exactly an instance of a class."""
	return isinstance(obj, a_class) and type(obj) is a_class
