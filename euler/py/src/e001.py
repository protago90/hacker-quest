#!/usr/bin/env python
# by protago90

from src.utils import promptify


def run_e1v1(x: int) -> int:
   rec: int = 0
   for n in range(x):
      if n % 3 == 0 or n % 5 == 0: rec += n
   return rec

def run_e1v2(x: int) -> int:
    return sum(
        filter(lambda n: n % 3 == 0 or n % 5 == 0, range(x)))

def run_e1v3(x: int) -> int:
    return sum(
        n for n in range(x) if n % 3 == 0 or n % 5 == 0)


@promptify
def solve_e1() -> int:
    '''
    Multiples of 5 and 3
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
    3, 5, 6 and 9. The sum of these multiples is 23.
    > Find the sum of all the multiples of 3 or 5 below 1000.
    ''' 
    return run_e1v1(1000)


if __name__ == '__main__':
    solve_e1()
    # >> the anwser for the #1 euler problem is >233168<; computed in 0.0001s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e1v1, run_e1v2, run_e1v3], args=[1000], i=10000)
    # >> the times of test solutions: run_e1v1=0.92s run_e1v2=1.30s run_e1v3=0.96s ∎
