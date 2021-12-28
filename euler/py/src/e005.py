#!/usr/bin/env python
# by protago90

from src.utils import promptify, prime_factors
from collections import defaultdict
from functools import reduce


def run_e5v1(x: int) -> int:
    cum = []
    for n in range(2, x+1):
        pf: list = prime_factors(n)
        for p in cum:
            if p in pf: 
                pf.remove(p)
        cum.extend(pf)
    return reduce(lambda i, j: i*j, cum)  # ~lcm

def run_e5v2(x: int) -> int:
    cum = defaultdict(int)
    rec = 1
    for n in range(2, x+1):
        pf: list = prime_factors(n)
        for p in set(pf):
            for _ in range(max(pf.count(p) - cum[p], 0)):
                cum[p] += 1
                rec *= p  # ~lcm
    return rec


@promptify
def solve_e5() -> int:
    '''
    Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.
    > What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    ''' 
    return run_e5v1(20)


if __name__ == '__main__':
    solve_e5()
    # >> the anwser for the #5 euler problem is >232792560<; computed in 0.0001s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e5v1, run_e5v2], args=[20], i=100000)
    # >> the times of test solutions: run_e5v1=5.85s run_e5v2=6.69s ∎
