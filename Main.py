import pygame as pg
import sys
from Const import *


class Main:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("CHESS")

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()

main = Main()
main.main_loop()
