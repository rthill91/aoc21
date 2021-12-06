import aoc21 as aoc
from aoc21.common import Movement


def test_day01_part1():
    test_input = [199,200,208,210,200,207,240,269,260,263]
    res = aoc.day01.part1(test_input)
    assert res == 7


def test_day01_part1():
    test_input = [199,200,208,210,200,207,240,269,260,263]
    res = aoc.day01.part2(test_input)
    assert res == 5


def test_day02_part2():
    test_input = [Movement("forward", 5), Movement("down", 5), Movement("forward", 8), Movement("up", 3), Movement("down", 8), Movement("forward", 2)]
    res = aoc.day02.part1(test_input)
    assert res == 150
