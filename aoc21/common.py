from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


@dataclass
class Movement:
    direction: Direction
    distance: int

    def __post_init__(self):
        if not isinstance(self.direction, Direction):
            self.direction = Direction(self.direction)


def get_input(day):
    file_name = f'input{str(day).zfill(2)}.txt'
    with open(f'./inputs/{file_name}') as fh:
        return fh.read().splitlines()


def get_int_input(day):
    return [int(i) for i in get_input(day)]


def get_movement_input(day):
    movements = []
    for line in get_input(day):
        split_line = line.split(" ")
        movements.append(Movement(split_line[0], int(split_line[1])))
    return movements

