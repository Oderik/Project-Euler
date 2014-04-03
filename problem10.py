from problem3 import *

__author__ = 'Oderik'



i = 0
p = 3
primes = [2]

while p < 2000000:
    if is_divisible(p, primes):
        primes.append(p)
        print(p)

    p += 2


print(sum(primes))