#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def primes():
    """calculate all primes"""
    primes = set()
    p = 2
    while True:
        for j in primes:
            if p % j == 0:
                break
        else:
            primes.add(p)
            yield p
        p += 1

i = 10001
for p in primes():
    i -= 1
    if i == 0:
        print(p)
        break
