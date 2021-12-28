#!/usr/bin/env python
# by protago90

from src.utils import is_prime, promptify, sieve_primes_gen


def run_e10v1(x: int) -> int:
    rec = 0
    for n in range(x):
        if is_prime(n): rec += n
    return rec

def run_e10v2(x: int, lim: int=10**7) -> int:  # awkwardly slow
    rec = 0
    for p in sieve_primes_gen(lim):
        if p < x:
            rec += p
        else: return rec


@promptify
def solve_e10() -> int:
    '''
    Summation of primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    > Find the sum of all the primes below two million.
    ''' 
    return run_e10v1(2000000)


if __name__ == '__main__':
    solve_e10()
    # >> the anwser for the #10 euler problem is >142913828922<; computed in 5.4386s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e10v1], args=[100000], i=1)
