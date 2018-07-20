#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        letter = sentence[0]
    else:
        letter = None
    length = len(sentence)
    tuple = (length, letter)
    return tuple
