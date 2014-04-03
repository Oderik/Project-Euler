__author__ = 'maik.riechel'


def difference(ceil):
    result = 0;
    for i in range(1, ceil + 1):
        for j in range(i + 1, ceil + 1):
            result += 2 * i * j
    return result

print(difference(100))