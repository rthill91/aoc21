from aoc21 import aoc
from aoc21.ship import Movement


def test_aoc():
    test_input = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    res = aoc.run(test_input)
    assert res == 230
