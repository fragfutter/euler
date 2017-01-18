#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def primes_to_n(n):
    """calculate all primes below n"""
    sieve = [1, ] * (n + 1)
    # special handling of 2 for faster looping
    sieve[2::2] = [0, ] * (n // 2)
    yield 2
    for i in range(3, n, 2):
        if not sieve[i]:
            continue  # not a prime
        sieve[i::i] = [0, ] * (n // i)
        yield i


print(sum(primes_to_n(8000000)))
