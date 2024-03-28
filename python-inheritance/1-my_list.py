#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """init class MyList"""

    def print_sorted(self):
        print(sorted(self))