#!/usr/bin/python3
"""
Module for MyList class that inherits from list. Adds functionality
to print elements in sorted order without altering the original list.
"""


class MyList(list):
    """
    Inherits from Python's built-in list. Adds method to print
    list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        print(sorted(self))
