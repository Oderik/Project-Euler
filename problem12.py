from itertools import count
from math import ceil

__author__ = 'Oderik'

def factors_of(n):
    if n <= 1:
        return [1]
    result = [1, n]
    for i in range(2, ceil((n + 1) / 2)):
        if n % i == 0:
            result.append(i)
    return result

def triangular(n):
    return n * (n+1) / 2

def findLowestTriangularWithFactors(min_factors):
    max_factors = 0
    for i in count(1):

        n = triangular(i)
        factors = len(factors_of(n))

        if factors > min_factors:
            return n
        elif factors > max_factors:
            max_factors = factors
            print(n, factors)


print(findLowestTriangularWithFactors(500))
