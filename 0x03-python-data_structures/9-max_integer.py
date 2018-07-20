#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        my_list.reverse()
        max_num = my_list[0]
        return max_num
    else:
        return None
