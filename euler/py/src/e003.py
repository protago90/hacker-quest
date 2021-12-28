#!/usr/bin/env python
# by protago90

from src.utils import promptify, sieve_primes, is_prime
from math import sqrt


def run_e3v1(x: int) -> int:
    lim = int(sqrt(x))
    for n in range(lim, 1, -1):
        if x % n == 0:
            if is_prime(n):
                return n

def run_e3v2(x: int) -> int:
    lim = int(sqrt(x))
    for p in sieve_primes(lim)[::-1]:
        if x % p == 0: 
            return p


@promptify
def solve_e3() -> int:
    '''
    Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    > What is the largest prime factor of the number 600851475143 ?
    ''' 
    return run_e3v1(600851475143)


if __name__ == '__main__':
    solve_e3()
    # >> the anwser for the #3 euler problem is >6857<; computed in 0.1104s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e3v1, run_e3v2], args=[13195], i=100000)
    # >> the times of test solutions: run_e3v1=0.63s run_e3v2=2.93s ∎
