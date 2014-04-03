__author__ = 'maik.riechel'
import problem3
import math


def flatten(primefactors):
    flattendprimefactors = {}
    for factor in primefactors:
        flattendprimefactors[factor] = flattendprimefactors.setdefault(factor, 0) + 1
    return flattendprimefactors


def merge(primefactors):
    mergedprimefactors = {}
    for p in primefactors:
        for key, value in p.items():
            mergedprimefactors[key] = max(value, mergedprimefactors.setdefault(key, 0))
    return mergedprimefactors



def smallestmultiple(factors):
    primefactors = []
    for factor in factors:
        if factor != 0:
            primefactors.append(flatten(problem3.primefactors(factor)))
    mergedprimefactors = merge(primefactors)
    result = 1
    for factor, power in mergedprimefactors.items():
        result *= factor ** power
    return result


print(20, smallestmultiple(range(1, 21)))