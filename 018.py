#!/usr/bin/python
import itertools

data1 = """
3
7 4
2 4 6
8 5 9 3
"""

data2 = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def data_to_int(data):
    for line in filter(None, data.split('\n')):
        yield(list(map(int, line.split(' '))))


def path_value(path, triangle):
    pos = 0
    result = 0
    for row in triangle:
        result += row[pos]
        pos += path & 1
        path = path >> 1
    return result


triangle = list(data_to_int(data2))
result = max([path_value(path, triangle) for path in range(2**(len(triangle) - 1))])
print(result)

# now intelligent
# take second to bottom row. 2 4 6
# if you are at the 2, you will move to 8, so replace 2 with 2+8=10; 10  4 6
# line becomes 2+8 4+9 6+9 = 10 13 15


def pairwise(i):
    """returns (i0, i1)  (i1,i2)  (i2, i3) ... (in-1, in)"""
    # see https://docs.python.org/3/library/itertools.html
    a, b = itertools.tee(i)
    next(b, None)
    return zip(a, b)

triangle.reverse()
previous = triangle[0]
for row in triangle[1:]:
    previous = [a + max(b) for a, b in zip(row, pairwise(previous))]
print(previous)
