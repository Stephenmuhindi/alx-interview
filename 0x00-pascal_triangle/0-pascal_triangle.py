#!/usr/bin/python3
"""
0-main
"""


def pascal_triangle(n):
    """
    A method that prints a list
    of integers that rep. the
    triangle of nnumber n:
       - prints the empty list if the num is 0
       - n ia assumed to be be an intx
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
                value = pascal_tri[i - 1][j - 1] + pascal_tri[i - 1][j]
                cur_row.append(value)

        pascal_tri.append(cur_row)

    return pascal_tri
