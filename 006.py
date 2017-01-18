#!/usr/bin/python
"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385 The square of the sum of the first ten natural
numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025 Hence the difference between the sum of the
squares of the first ten natural numbers and the square of the sum is 3025 −
385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
stop = 100

# a = sum(range(1, stop + 1))
a = stop * (stop + 1) // 2
a = a ** 2

b = sum([i * i for i in range(1, stop + 1)])
print(a - b)
