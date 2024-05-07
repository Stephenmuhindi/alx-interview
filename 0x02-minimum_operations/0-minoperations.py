#!/usr/bin/python3
"""
i think that this is the best mode
factorize the number n and increment op
"""


def minOperations(n: int) -> int:
    """
    fewest number of operations to result in that
    """
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
