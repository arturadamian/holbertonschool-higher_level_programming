#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    sum_tuple = tuple(sum(x) for x in zip(tuple_a, tuple_b))
    return sum_tuple
