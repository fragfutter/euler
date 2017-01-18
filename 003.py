#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def primes(data):
    """calculate all primes below data"""
    negatives = set()
    for i in range(2, data):
        if i in negatives:
            continue
        yield i
        negatives.update(range(i * i, data, i))

x = 600851475143
i = 2
while i < x:
    while x % i == 0:
        x = x // i
        print(i)
    i += 1
print(i)
