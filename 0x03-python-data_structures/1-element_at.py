#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(my_list):
        if idx < 0 or idx > range(my_list) - 1:
            return None
        else:
             my_list[idx]

