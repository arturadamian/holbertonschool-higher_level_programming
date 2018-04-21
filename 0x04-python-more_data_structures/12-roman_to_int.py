#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    di_roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    special = 0
    integer = 0
    for i in roman_string:
        if special < di_roma[i]:
            integer -= special * 2
        special = di_roma[i]
        integer += di_roma[i]
    return integer
