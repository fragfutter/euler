#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

top = 1000
for a in range(1, top):
    for b in range(a, top):
        c = top - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c, a * b * c)
