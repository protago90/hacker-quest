#!/usr/bin/env python
# by protago90

from src.utils import promptify
from math import sqrt


def run_e9v1(x: int) -> int:
    lim = int(x/2)
    for a in range(1, lim):
        for b in range(1, a):
            c = sqrt(a**2 + b**2)
            if a+b+c == x:
                return int(a*b*c)


@promptify
def solve_e9() -> int:
    '''
    Special Pythagorean triplets
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
    a^2 + b^2 = c^2. For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    > There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
    Find the product abc.
    ''' 
    return run_e9v1(1000)


if __name__ == '__main__':
    solve_e9()
    # >> the anwser for the #9 euler problem is >31875000<; computed in 0.0424s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e1v1], args=[1000], i=10000)
