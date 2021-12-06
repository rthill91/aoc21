from .ship import Movement


def get_input(day):
    file_name = f'input{str(day).zfill(2)}.txt'
    with open(f'./inputs/{file_name}') as fh:
        return fh.read().splitlines()


def get_movement_input(day):
    movements = []
    for line in get_input(day):
        split_line = line.split(" ")
        movements.append(Movement(split_line[0], int(split_line[1])))
    return movements

