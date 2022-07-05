#!/usr/bin/python3
"""Module 1-my_list.py
A 'my_list' class that inherits from
a super class 'list'
"""


class MyList(list):
    """Inherits from list class"""
    def print_sorted(self):
        """Prints a sorted list"""
        n_list = self[:]
        n_list.sort()
        print("{}".format(n_list)
