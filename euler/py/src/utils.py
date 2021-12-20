# by protago90

from time import time
from timeit import timeit
from typing import Callable, List
from functools import partial

MSG = '  >> {}∎'


# Utils

def promptify(f: Callable) -> Callable:
    '''
    Handler of euler's problem dedicated [f]unc to print solution and computing time.
    '''
    def f_n(*args, **kwargs) -> None:
        n = int(''.join(filter(str.isdigit, f.__name__)))
        t = time()
        m = (f'the anwser for the #{n} euler problem is >{f(*args, **kwargs)}<; '
             f'computed in {round(time() - t, 4):.4f}s ')
        print(MSG.format(m))
    return f_n


def timeitfy(fs: List[Callable], args, i: int=10) -> None:
    '''
    Tester of time performance of proposed [f]unc[s] with euler's solutions.
    '''
    assert len(fs) > 0
    m = f'the times of test solutions: '
    for f in fs:
        m += f'{f.__name__}={round(timeit(partial(f, *args), number=i), 2):.2f}s '
    print(MSG.format(m))
