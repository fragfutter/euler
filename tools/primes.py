import math
import numpy
import itertools


def primes_below(n):
    """all prime numbers below n"""
    # see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    #
    # check for even numbers, allows iteration in steps of two
    if n < 2:
        return
    yield 2
    sieve = numpy.ones(n, dtype=numpy.bool)
    # as we already checked for two, we can step every second
    for i in range(3, n, 2):
        if sieve[i]:
            yield i
            # all numbers to square(i) are already marked
            sieve[i * i::2 * i] = False
    # TODO optimize to use a half/sieve


def primes_generator():
    """unbound primes generator"""
    # see
    # http://archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
    # itertools.takewhile(lambda p: p < n, primes.primes_generator())
    D = {}
    for q in itertools.count(2):
        p = D.pop(q, None)
        if p is None:
            yield q
            D[q * q] = q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p


def is_prime(n):
    """test if n is a prime number"""
    if n == 1:
        return False
    if n < 4:
        return True  # 2, 3 are primes
    if n % 2 == 0:
        return False  # even numbers
    if n < 9:
        return True  # 2, 3, 4, 6, 8 are done. leaves 5, 7 which are primes
    if n % 3 == 0:
        return False  # multiples of three
    # all primes greater then 3 can be written as 6*k +- 1
    # any number n can only have one factor above sqrt(n)
    limit = int(math.sqrt(n))
    # loop in steps of six with an offset of -1
    for i in range(5, limit, 6):
        if n % i == 0:  # 6k - 1
            return False
        if n % (i + 2) == 0:  # 6k + 1
            return False
    return True
