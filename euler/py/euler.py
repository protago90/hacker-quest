#!/usr/bin/python
# by protago90

from argparse import ArgumentParser, Namespace
from typing import Callable, List
from src import *  # i.e. all solvers from src/E??.py


class Solver():
    e1:  Callable = e001.solve_e1   # Multiples of 5 and 3

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
