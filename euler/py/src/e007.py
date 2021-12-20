#!/usr/bin/env python
# by protago90

from src.utils import promptify, sieve_primes_gen


def run_e7v1(x: int, lim: int=1000000) -> int:
    for i, p in enumerate(sieve_primes_gen(lim)):
        if i+1 == x:
            return p


@promptify
def solve_e7() -> int:
    '''
    10001st
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
    the 6th prime is 13.
    > What is the 10 001st prime number?
    ''' 
    return run_e7v1(10001)


if __name__ == '__main__':
    solve_e7()
    # >> the anwser for the #7 euler problem is >104743<; computed in 2.8358s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e7v1], args=[10001], i=10)
