from Const import *
from Square import Square


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self.create()

    # A private method
    def create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.square[row][col] = Square(row, col)

    # A private method
    def add_pieces(self, color):
        pass
