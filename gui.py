from random import random
from pprint import pprint as pp

import pygame
from ChoToTam1 import Pole
from ChoToTam1 import Kletka


class GUI:
    def __init__(self):
        self.game_pole = Pole(30, 30)
        self.width, self.height = self.game_pole.wifth_and_height()
        self.screen = pygame.display.set_mode((self.width*18, self.height*18+200))

    def p(self):
        x = 0
        y = 0
        for a in range(self.height):
            for b in range(self.width):
                if self.game_pole.kletka(a, b).sost() == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("red")
                pygame.draw.rect(self.screen, color, (x, y, 15, 15))
                x += 18
            y += 18
            x = 0
        pygame.display.flip()


if __name__ == '__main__':
    gui = GUI()
    gui.p()
    while 1:
        pass