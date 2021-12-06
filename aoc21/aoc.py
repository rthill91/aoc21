from .common import get_movement_input
from .ship import Ship, Movement, Direction


def run(test_input=None):
    if test_input:
        movement = test_input
    else:
        movement = get_movement_input(2)
    ship = Ship()

    for move in movement:
        ship.move(move)
    hash = ship.get_hash()
    print(hash)
    return hash
