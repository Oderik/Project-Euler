SMALLEST_PRIME = 2
__author__ = 'maik.riechel'
import math


def is_divisible(n, candidates):
    half_n = n / 2
    for x in candidates:
        if x > half_n:
            print(x, half_n, n)
            return True
        if n % x == 0:
            return False
    return True


def is_prime(n):
    if n < SMALLEST_PRIME:
        return False
    half = math.ceil(n / SMALLEST_PRIME)
    candidates = range(SMALLEST_PRIME, half + 1)
    return is_divisible(n, candidates)


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