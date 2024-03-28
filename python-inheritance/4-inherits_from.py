#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """inherits_from function"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class