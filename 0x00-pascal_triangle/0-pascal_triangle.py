#!/usr/bin/python3
"""Pascal's half square"""


def pascal_triangle(n):
    """
    A function that returns a list
    of integers that print a triangle
    """
    pascal_tri = []

    if n <= 0:
        return []

    for i in range(n):
        cur_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                cur_row.append(1)
            else:
                value = int(pascal_tri[i - 1][j - 1] * (i - j + 1) / j)
                cur_row.append(value)

        pascal_tri.append(cur_row)

    return pascal_tri

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))
