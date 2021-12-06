from aoc21 import aoc
from aoc21.ship import Movement


def test_aoc():
    test_input = [Movement("forward", 5), Movement("down", 5), Movement("forward", 8), Movement("up", 3), Movement("down", 8), Movement("forward", 2)]
    res = aoc.run(test_input)
    assert res == 150
