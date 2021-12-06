from collections import Counter
from .common import get_input
from .ship import Ship, Movement, Direction


def run(test_input=None):
    if test_input:
        _input = test_input
    else:
        _input = get_input()

    zipped = zip(*[list(c) for c in _input])
    gamma_str = ''
    epsilon_str = ''
    for c in zipped:
        counter = Counter(c)
        gamma_str += max(counter, key=counter.get)
        epsilon_str += min(counter, key=counter.get)

    gamma_rate = int(gamma_str, 2)
    epsilon_rate = int(epsilon_str, 2)

    res = gamma_rate * epsilon_rate
    print(res)
    return res

