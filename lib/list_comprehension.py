#!/usr/bin/env python3

def return_evens(lst):
    return [num for num in lst if num % 2 == 0]


def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]
