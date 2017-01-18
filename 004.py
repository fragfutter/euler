#!/usr/bin/python
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(start, stop):
    result = 0
    for i in range(stop, start, -1):
        if i * stop < result:
            # we can't find anything bigger than result
            break
        for j in range(stop, i, -1):
            if i * j < result:
                # we can't find anything bigger than result
                break
            pn = i * j
            if pn < result:
                # faster to test then stringifying
                continue
            ps = str(pn)
            if ps == ps[::-1]:
                if pn > result:
                    result = pn
    return result

print(palindrome(100, 1000))
