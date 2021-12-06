from collections import Counter
from .common import get_input
from .ship import Ship, Movement, Direction
from copy import copy


def run(test_input=None):
    if test_input:
        _input = test_input
    else:
        _input = get_input()

    oxygen_str = _get_life_support_value(copy(_input), max, '1')
    co2_str = _get_life_support_value(_input, min, '0')
    oxygen = int(oxygen_str, 2)
    co2 = int(co2_str, 2)
    res = oxygen * co2
    print(res)
    return res


def _get_life_support_value(_input, fn, default):
    for i in range(len(_input[0])):
        bits = [c[i] for c in _input]
        idxs = _get_value(bits, fn, default)
        for i in sorted(idxs, reverse=True):
            _input.pop(i)
    return _input[0]



def _get_value(bits, fn, default):
    counter = Counter(bits)
    res = _default_min_max(counter, fn, default)
    return [i for i,x in enumerate(bits) if x != res]


def _default_min_max(counter, fn, default):
    if counter['0'] == counter['1']:
        return default
    return fn(counter, key=counter.get)
