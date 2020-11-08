from random import random
from pprint import pprint as pp

import pygame
from ChoToTam1 import Pole


game = -1
fps = 1

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
        global game
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    fps += 0.1
                if i.key == pygame.K_DOWN:
                    fps -= 0.1
                if i.key == pygame.K_RIGHT:
                    gui.hod()
                    gui.p()
                if i.key == pygame.K_SPACE:
                    game *= -1
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    pos = pygame.mouse.get_pos()
                    y = pos[1] // 18
                    x = pos[0] // 18
                    sos = 0
                    if self.game_pole.kletka(y, x).sost() == 0:
                        sos = 1
                    self.game_pole.kletka(y, x).next_sost(sos)
                    self.game_pole.kletka(y, x).old_to_new()
                    gui.p()
                if i.button == 3:
                    for x in range(self.width):
                        for y in range(self.height):
                            self.game_pole.kletka(y, x).next_sost(0)
                            self.game_pole.kletka(y, x).old_to_new()
                    gui.p()

def bin(x):
    ch = []
    while(x != 0):
        if ch != 1:
            y = x % 2
            ch.append(y)
            x //= 2
        else:
            ch.append(1)
            ch = 0
    return ch


if __name__ == '__main__':
    pause = pygame.time.Clock()
    gui = GUI()
    gui.p()
    while (True):
        gui.event()
        if game > 0:
            gui.hod()
            gui.p()
            pause.tick(fps)

