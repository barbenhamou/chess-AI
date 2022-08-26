import pygame as pg
import sys
from Const import *
from Game import Game


class Main:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("CHESS")
        self.game = Game()

    def main_loop(self):
        game = self.game
        screen = self.screen

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()


main = Main()
main.main_loop()
