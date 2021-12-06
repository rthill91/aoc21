from .common import get_bingo_input
from .ship import Ship, Movement, Direction
from .bingo import Bingo
from copy import copy


def run(test_input=None):
    numbers, boards = get_bingo_input()
    bingo = Bingo(numbers, boards)
    score = bingo.play()
    print(score)
    return score
