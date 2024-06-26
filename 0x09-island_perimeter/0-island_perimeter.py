#!/usr/bin/python2
"""
module definition
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """
    Find cell with either 4, 3, 2 or 1.
    """
    boundaries = 0
    if i == 0 or grid[i-1][j] == 0:
        boundaries += 1
    if i == len(grid) - 1 or grid[i+1][j] == 0:
        boundaries += 1
    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
        boundaries += 1
    if j == 0 or grid[i][j-1] == 0:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    Calculate and return perimeter of island in the grid
    """
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if bound_4:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
