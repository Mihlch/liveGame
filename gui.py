from random import random
from pprint import pprint as pp

import pygame
from ChoToTam1 import Pole


game = True
fps = 0.1

class GUI:
    def __init__(self):
        self.game_pole = Pole(30, 30)
        self.width, self.height = self.game_pole.wifth_and_height()
        self.screen = pygame.display.set_mode((self.width * 18, self.height * 18 + 200))

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

    def hod(self):
        self.game_pole.hod()

    def event(self):
        global fps
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    fps += 0.1
                elif i.key == pygame.K_DOWN:
                    fps -= 0.1
                elif i.key == pygame.K_SPACE:
                    fps = 0


if __name__ == '__main__':
    pause = pygame.time.Clock()
    gui = GUI()
    while (game):
        gui.p()
        gui.hod()
        gui.event()
        pause.tick(fps)
