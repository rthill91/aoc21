from .common import get_movement_input, Movement, Direction


class Ship():
    def __init__(self):
        self._x = 0
        self._y = 0

    def get_coords(self) -> tuple[int, int]:
        return (self._x, self._y)

    def get_hash(self) -> int:
        return self._x * self._y

    def move(self, movement: Movement):
        match movement.direction:
            case Direction.FORWARD:
                self._x += movement.distance
            case Direction.UP:
                self._y -= movement.distance
            case Direction.DOWN:
                self._y += movement.distance


def run():
    inputs = get_movement_input(2)
    part1(inputs)


def part1(movement: Movement):
    ship = Ship()
    for move in movement:
        ship.move(move)
    hash = ship.get_hash()
    print(hash)
    return hash


def part2():
    return NotImplemented
