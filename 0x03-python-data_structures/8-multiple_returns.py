#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_chr = None
    else:
        first_chr = sentence[0]
    data = (length, first_chr)
    return data
