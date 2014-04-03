SMALLEST_PRIME = 2
__author__ = 'maik.riechel'
import math


def is_prime(n):
    if n < SMALLEST_PRIME:
        return False
    half = math.ceil(n / SMALLEST_PRIME)
    for x in range(SMALLEST_PRIME, half + 1):
        if n % x == 0:
            return False
    return True


def next_prime(p):
    if p < SMALLEST_PRIME:
        return SMALLEST_PRIME
    if p == SMALLEST_PRIME:
        return 3
    nextp = p + 2
    while not is_prime(nextp):
        nextp += 2
    return nextp


def primefactors(m):
    n = m
    prime = SMALLEST_PRIME
    factors = []
    while n > 1:
        if n % prime == 0:
            factors = factors + [prime]
            n //= prime
            # print(m, "=", n, "*", factors)
        else:
            prime = next_prime(prime)
    return factors


def main():
    i = 39486392752340985
    print(i, ": ", primefactors(i))


if __name__ == "__main__":
    main()