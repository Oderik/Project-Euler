__author__ = 'maik.riechel'

def faculty(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def binomial_coefficient(n, k):
    return faculty(n) / (faculty(k) * faculty(n-k))

def latize(width, height):
    return binomial_coefficient(width + height, width)

print(latize(20, 20))