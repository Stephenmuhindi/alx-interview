#!/usr/bin/python3
"""
Rotates a 2D square matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(m):
    """
    takes a 2D matrix m as input and performs
    the rotation
    """
    width = len(m[0])
    height = len(m)
    total_items = width * height
    map_ = build_map(m, total_items, width)
    # print(map_)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, index = compute_row_and_index(new_index, width)
        m[row][index] = value


def build_map(m, length, width):
    """
    builds a dictionary that maps each index
    in the original matrix to its new index after rotation.
    It also stores the original value at that index
    """
    dct = {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }
    return dct


def get_new_index(i, width):
    """
    calculates the new index for a given index
    in the original matrix based on its width
    """
    current_index = i % width
    current_row = int(i / width)
    next_index = width - 1 - current_row
    next_row = current_index
    next_position = next_row * width + next_index
    return next_position


def get_value(m, i, width):
    """
    retrieves the value from the original matrix
    at a given index i based on its width
    """
    current_index = i % width
    current_row = int(i / width)
    return m[current_row][current_index]


def compute_row_and_index(flat_index, width):
    """
    converts a flattened index
    (single index representing a row-column pair)
    back to its original row and column position
    based on the width
    """
    row = int(flat_index / width)
    index = flat_index % width
    return row, index


def printx(lst):
    """ print the 2D matrix in a user-friendly format"""
    print("[")
    for itm in lst:
        print("  ", str(itm) + ",")
    print("]")


def build_matrix(n):
    """ builds an n x n matrix filled with sequential numbers"""
    parent = []
    y = 1
    for i in range(n):
        child = []
        for x in range(y, n * n + 1):
            child.append(x)
            if x % n == 0 and x != 1:
                y = x + 1
                break
        parent.append(child)
    return parent


if __name__ == "__main__":
    matrix = build_matrix(3)

    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = build_matrix(5)

    rotate_2d_matrix(matrix)
    printx(matrix)
