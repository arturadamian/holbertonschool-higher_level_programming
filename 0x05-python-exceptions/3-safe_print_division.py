#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        count = a / b
    except(ZeroDivisionError):
        count = None
    finally:
        print("Inside result: {}".format(count))
    return count
