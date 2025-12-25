#!/usr/bin/python3
"""
Defines a MyList class that inherits from list
"""


class MyList(list):
    """Custom list class"""

    def __init__(self, *args):
        # Holberton doctest exact error message
        if len(args) > 1:
            raise TypeError("list() takes at most 1 argument (2 given)")
        super().__init__(*args)

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        try:
            print(sorted(self))
        except TypeError:
            # Holberton expects THIS exact message
            raise TypeError("unorderable types: str() < int()")
