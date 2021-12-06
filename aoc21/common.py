from .ship import Movement


def get_input():
    with open('./input.txt') as fh:
        return fh.read().splitlines()


def get_movement_input():
    movements = []
    for line in get_input():
        split_line = line.split(" ")
        movements.append(Movement(split_line[0], int(split_line[1])))
    return movements
