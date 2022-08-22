import pygame as pg

from Const import *


class Game:

    def __init__(self):
        self.next_player = None
        self.game_mode = None

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pg.draw.rect(surface, color, rect)

    def show_pieces(self):
        pass

    def show_moves(self):
        pass

    def show_last_move(self):
        pass

    def show_hover(self):
        pass

    def next_turn(self):
        pass

    def set_hover(self):
        pass

    def change_theme(self):
        pass

    def play_sound(self):
        pass

    def reset(self):
        pass

    def change_game_mode(self):
        pass
