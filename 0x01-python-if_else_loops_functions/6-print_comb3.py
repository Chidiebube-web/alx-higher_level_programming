#!/usr/bin/python3
for int in range(0, 9):
    for rem in range(int + 1, 10):
        if int == 8:
            print("{}{}".format(int, rem))
        else:
            print("{}{}".format(int, rem), end=', ')
