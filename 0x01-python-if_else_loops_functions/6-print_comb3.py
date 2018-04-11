#!/usr/bin/python3
for i in range(1, 99):
    div = i / 10
    mod = i % 10
    if (div < mod):
        if (i != 89):
            print("{:02d}".format(i), end=', ')
        else:
            print("{}".format(i))
