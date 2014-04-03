__author__ = 'maik.riechel'


def latize_paths(grid_size):
    if grid_size == 1:
        return 2
    smaller_grid = grid_size - 1
    return (latize_paths(smaller_grid) + smaller_grid) * 2


print(latize_paths(20))