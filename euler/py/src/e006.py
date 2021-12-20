#!/usr/bin/env python
# by protago90

from src.utils import promptify


def run_e6v1(x: int) -> int:
    rng = range(1, x+1)
    return sum(rng)**2 - sum(n**2 for n in rng)

def run_e6v2(x: int) -> int:
    s, s_sq = 0, 0
    for n in range(1, x+1):
        s += n
        s_sq += n**2
    return s**2 - s_sq


@promptify
def solve_e6() -> int:
    '''
    Sum square difference
    The sum of the squares of the first ten natural numbers is 
    1^2 + 2^2 + ... + 10^2 = 385.
    The square of the sum of the first ten natural numbers is
    (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025 − 385 = 2640.
    > Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    ''' 
    return run_e6v1(100)


if __name__ == '__main__':
    solve_e6()
    # >> the anwser for the #6 euler problem is >25164150<; computed in 0.0000s ∎

    # from src.utils import timeitfy
    # timeitfy([run_e6v1, run_e6v2], args=[100], i=100000)
    # >> the times of test solutions: run_e6v1=2.91s run_e6v2=3.11s ∎
