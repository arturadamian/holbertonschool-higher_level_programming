#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        letter = sentence[0]
    else:
        letter = None
    tuple = (len(sentence), sentence[0])
    return tuple
