#!/usr/bin/env python
# by protago90

from src.utils import promptify


def run_e4v1(x: int) -> int:
    rec = 1
    t, tt  = 10**(x-1), 10**x - 1
    for n in range(t, tt):
        for m in range(n, tt):
            p = n * m
            if p == int(str(p)[::-1]) & p > rec:
                rec = p 
    return rec 


@promptify
def solve_e4() -> int:
    '''
    Largest polindrome product  
    A palindromic number reads the same both ways. The largest palindrome made from
    the product of two 2-digit numbers is 9009 = 91 × 99.
    > Find the largest palindrome made from the product of two 3-digit numbers.
    ''' 
    return run_e4v1(3)


if __name__ == '__main__':
    solve_e4()
    # >> the anwser for the #4 euler problem is >906609<; computed in 0.2008s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e4v1], args=[3], i=10000)
