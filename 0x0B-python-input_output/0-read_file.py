#!/usr/bin/python3
"""Module 0-read_file
Reads a text file"""


def read_file(filename=''):
    """This function reads a text file
    in the UTF-8 encoding format and 
    prints it to stdout 
    """

    with open(filename) as text_file:
        data = text_file.read()
        print(data, end="")
