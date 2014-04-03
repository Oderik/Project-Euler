__author__ = 'maik.riechel'

import problem3


def getprime(count):
    prime = 2
    while count > 1:
        count-=1
        prime = problem3.next_prime(prime)
    return prime


print(getprime(10001))