__author__ = 'maik.riechel'

def triangular(n):
    return n * (n + 1) / 2

def latize_paths(grid_size):
    if grid_size == 1:
        return 2
    smaller_grid = grid_size - 1
    return (latize_paths(smaller_grid) + smaller_grid) * 2

result = 0

def latize(width, height):
    result = 1
    slots = (width + height)
    for n in range(width + height, width, -1):
        result *= n
        print(n, result)
    return result

print(latize(2, 2))