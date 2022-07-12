#!/usr/bin/python3
"""Module base
This creates a base class
that will be the root of all
the projects.
"""


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of an instance
        """
        if type(id) != None and id is not None:
            raise TypeError("id has to be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
