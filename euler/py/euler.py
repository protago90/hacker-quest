#!/usr/bin/python
# by protago90

from argparse import ArgumentParser, Namespace
from typing import Callable, List
from src import *  # i.e. all solvers from src/E*.py


class Solver():
    e1:  Callable = e001.solve_e1   # Multiples of 5 and 3    
    e2:  Callable = e002.solve_e2   # Even Fibonacci numbers
    e3:  Callable = e003.solve_e3   # Largest prime factor
    e4:  Callable = e004.solve_e4   # Largest polindrome product
    e5:  Callable = e005.solve_e5   # Smallest multiple
    e6:  Callable = e006.solve_e6   # Sum square difference
    e7:  Callable = e007.solve_e7   # 10001st
    e8:  Callable = e008.solve_e8   # Largest product in a series
    e9:  Callable = e009.solve_e9   # Special Pythagorean triplets
    e10: Callable = e010.solve_e10  # Summation of primes

    @classmethod
    def run(cls, n: str) -> None:
        return getattr(cls, n)()

    @classmethod
    def get_done(cls) -> List[int]:
        return [int(''.join(filter(str.isdigit, k))) for k, v in cls.__dict__.items()
                if not k.startswith('__') and callable(v)]


def parse_args() -> Namespace:
    s: List[int] = Solver.get_done()
    a = ArgumentParser()
    a.add_argument('-p', '--problem', required=True, type=int, choices=s)
    return a.parse_args()


if __name__ == '__main__':
    euler_problem: str = 'e{:01d}'.format(parse_args().problem)
    Solver.run(n=euler_problem)
