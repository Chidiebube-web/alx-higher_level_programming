#!/usr/bin/python3
"""1-rectangle Module
Defines a rectangle with
an input height and width
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def width(self):
        """Returns the value of the width"""
        return self.__width
    def width(self, value):
        if type(value) != int:
            """Returns a typeerror if NaN"""
            return "TypeError: width must be an integer"
        elif value < 0:
            """Returns a valueerror if value is less than 0"""
            return "ValueError: width must be >= 0"
        else:
            """Sets the width value"""
            self.value = value
    def height(self):
        """Returns the value of the height"""
        return self.__height
    def height(self, value):
        if type(value) != int:
            """returns a typeerror if value is NaN"""
            return "TypeError: height must be an integer"
        elif value < 0:
            """returns a valueerror if value is less than 0"""
            return "ValueError: height must be >= 0"
        else:
            """sets the height value"""
            self.value = value
