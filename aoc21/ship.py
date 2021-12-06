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


class Ship():
    def __init__(self):
        self._x = 0
        self._y = 0
        self._aim = 0

    def get_coords(self) -> tuple[int, int]:
        return (self._x, self._y)

    def get_hash(self) -> int:
        return self._x * self._y

    def move(self, movement: Movement):
        match movement.direction:
            case Direction.FORWARD:
                self._x += movement.distance
                self._y += movement.distance * self._aim
            case Direction.UP:
                self._aim -= movement.distance
            case Direction.DOWN:
                self._aim += movement.distance
