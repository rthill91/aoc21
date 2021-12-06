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


def get_bingo_input():
    boards = []
    numbers = []
    _board = []
    for line in get_input():
        if not line:
            continue
        if not numbers:
            numbers = [int(i) for i in line.split(',')]
            continue
        if len(_board) == 5:
            boards.append(_board)
            _board = []
        _board.append(line)
    boards.append(_board)
    return (numbers, boards)



