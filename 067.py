#!/usr/bin/python
import itertools


def parse_triangle():
    data = open('067.txt', 'r').readlines()
    for line in data:
        yield(list(map(int, line.split(' '))))


def pairwise(i):
    """returns (i0, i1)  (i1,i2)  (i2, i3) ... (in-1, in)"""
    # see https://docs.python.org/3/library/itertools.html
    a, b = itertools.tee(i)
    next(b, None)
    return zip(a, b)

triangle = list(parse_triangle())
triangle.reverse()
previous = triangle[0]
for row in triangle[1:]:
    previous = [a + max(b) for a, b in zip(row, pairwise(previous))]
print(previous)
