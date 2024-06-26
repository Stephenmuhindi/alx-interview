#!/usr/bin/python3
"""
module definition
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """
    find cells with 4 factorial
    """
    boundaries = 0
    try:
        if i == 0:
            boundaries += 1
        elif grid[i-1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if grid[i+1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if grid[i][j+1] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if j == 0:
            boundaries += 1
        elif grid[i][j-1] == 0:
            boundaries += 1
    except IndexError:
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
    Calculate and return perimeter of island
    """
    if grid == []:
        return 0
    row = len(grid)
    coll = len(grid[0])
    for i in range(row):
        for j in range(coll):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
