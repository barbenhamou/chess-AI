import pygame as pg
from Board import Board
from Const import *


class Game:

    def __init__(self):
        self.next_player = None
        self.game_mode = None
        self.board = Board()


    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (255, 255, 255)
                else:
                    color = (56, 67, 233)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pg.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # What piece?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pg.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)

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
