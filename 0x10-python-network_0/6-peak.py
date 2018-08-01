#!/usr/bin/python3
# find a peak


def find_peak(list_of_integers):
    """find the peak of list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    l = list_of_integers
    if len(l) == 1:
        return l[0]
    i = int(len(l)/2)
    if len(l) == 2:
        return l[0] if l[0] > l[1] else l[1]
    if l[i - 1] <= l[i] >= l[i + 1]:
        return l[i]
    else:
        if l[i] < l[i + 1]:
            return find_peak(l[i:])
        else:
            return find_peak(l[:i])
