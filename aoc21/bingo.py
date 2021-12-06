from dataclasses import dataclass
from collections import Counter, defaultdict


@dataclass
class Spot:
    x: int
    y: int
    marked: bool = False

    def mark(self):
        self.marked = True



class Board:
    def __init__(self, board):
        self._board = {}
        for y, row in enumerate(board):
            for x, num in enumerate(row.split()):
                num = int(num.strip())
                self._board[num] = Spot(x, y, False)

    def mark_number(self, number):
        if number not in self._board:
            return
        self._board[number].mark()

    def is_win(self):
        x_counts = defaultdict(int)
        y_counts = defaultdict(int)
        for num, spot in self._board.items():
            if not spot.marked:
                continue
            x_counts[spot.x] += 1
            y_counts[spot.y] += 1
        if 5 in x_counts.values() or 5 in y_counts.values():
            return True
        return False

    def get_score(self, winning_number):
        score = 0
        for num, spot in self._board.items():
            if not spot.marked:
                score += num
        return score * winning_number


class Bingo:
    def __init__(self, numbers, boards):
        self._boards = [Board(b) for b in boards]
        self._numbers = numbers

    def play(self):
        marked_for_removal = []
        for num in self._numbers:
            marked_for_removal.clear()
            for i, board in enumerate(self._boards):
                board.mark_number(num)
                if board.is_win():
                    marked_for_removal.append(i)

            for r in sorted(marked_for_removal, reverse=True):
                b = self._boards.pop(r)
                if len(self._boards) == 0:
                    return b.get_score(num)
