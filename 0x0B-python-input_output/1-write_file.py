#!/usr/bin/python3
"""Module 1-write_file
Returns number of lines in a file
"""


def write_file(filename="", text=""):
    """A function that returns the number
    of characters written in a text file
    """
    number = 0

    with open(filename) as text:
        lines = text.readlines()
        for i in lines:
            number += 1

    return number

