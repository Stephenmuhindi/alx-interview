#!/usr/bin/python3
"""
Module description
"""


def primes(n):
    """
    Finds all prime numbers from 2 to n (inclusive).
    """
    prime = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [p for p, is_prime in enumerate(sieve) if is_prime]


def is_winner(x, nums):
    """
    winner is
    """

    if x is None or nums is None or not nums:
        return None

    maria_score = 0
    ben_score = 0
    for num in nums:
        prime_count = 0
        for factor in range(2, int(num**0.5) + 1):
            if num % factor == 0:
                prime_count += 1
                num //= factor
                while num % factor == 0:
                    num //= factor
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
