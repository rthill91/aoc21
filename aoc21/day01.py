from .common import get_int_input

Measurements = list[int]

def run():
    inputs = get_int_input(1)
    part1(inputs)
    part2(inputs)


def part1(measurements: Measurements) -> int:
    pairs = zip(measurements, measurements[1:])
    res = len([p for p in pairs if p[1] > p[0]])
    print(res)
    return res


def part2(measurements: Measurements) -> int:
    windows = zip(measurements, measurements[1:], measurements[2:])
    sums = [sum(w) for w in windows]
    res = len([s for s in zip(sums, sums[1:]) if s[1] > s[0]])
    print(res)
    return res
