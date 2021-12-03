import aoc21 as aoc


def test_day01_part1():
    test_input = [199,200,208,210,200,207,240,269,260,263]
    res = aoc.day01.part1(test_input)
    assert res == 7


def test_day01_part1():
    test_input = [199,200,208,210,200,207,240,269,260,263]
    res = aoc.day01.part2(test_input)
    assert res == 5
