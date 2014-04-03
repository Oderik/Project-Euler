__author__ = 'maik.riechel'

def ispalindromic(n):
    s = str(n)
    if len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            return ispalindromic(s[1:-1])
    else:
        return True


maxproduct, maxi, maxj = 0, 0, 0

for i in range(1000):
    for j in range(1000):
        product = i * j
        if ispalindromic(product):
            if product > maxproduct:
                maxproduct, maxi, maxj = product, i, j
            print(product, '=', i, '*', j)
print(maxproduct, maxi, maxj)