#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    val = {}
    for i in a_dictionary:
        val[i] = a_dictionary[i] * 2
    return val
