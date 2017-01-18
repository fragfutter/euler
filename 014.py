#!/usr/bin/python
import itertools


cache = {}


def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


def cached_len_collatz(n):
    key = n
    result = 0
    while n != 1:
        if n in cache:
            result += cache[n]
            break
        result += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    else:
        # looped to 1, add the 1 itself
        result += 1
    cache[key] = result
    return result


m = (0, 0)
for i in itertools.count(1):
    if i > 1000000:
        break
    l = cached_len_collatz(i)
    # l = len(list(collatz(i)))
    if m[0] < l:
        m = (l, i)
print(m)
