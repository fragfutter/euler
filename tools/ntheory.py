from .primes import primes_generator


def factorint(n, table=None):
    """return dictionary {a1: x1, as: x2, ..} such that
    n = a1**x1 * a2**x2
    where each a is a prime number

    if a table of prime exists, it can be used, otherwise
    primes are generated on each run
    """
    # alternative sympy.ntheory.factorint
    if table:
        primes = table
    else:
        primes = primes_generator()
    result = {}
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            result[p] = 0
            while n % p == 0:
                result[p] += 1
                n = n // p
    return result
