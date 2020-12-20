from random import random
from pprint import pprint as pp

import pygame
from ChoToTam1 import Pole

game = -1
fps = 2
width = 50
height = 50
znat = []
hod = 0
anim = []


class GUI:
    def __init__(self):
        self.game_pole = Pole(width, height)
        self.width, self.height = self.game_pole.wifth_and_height()
        self.screen = pygame.display.set_mode((self.width * 18, self.height * 18 + 200))

    def p(self):
        x = 0
        y = 0
        for a in range(self.width):
            for b in range(self.height):
                if self.game_pole.kletka(a, b).sost() == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("red")
                pygame.draw.rect(self.screen, color, (x, y, 15, 15))
                x += 18
            y += 18
            x = 0
        pygame.display.flip()

    def zap(self):
        global znat
        n=[]
        for y in range(self.width):
            for x in range(self.height):
                n.append(self.game_pole.kletka(x, y).sost())
        n.reverse()
        if len(znat) <= hod:
            znat.append(des(n))
        else:
            znat[hod]= des(n)

    def hod(self):
        self.zap()
        self.game_pole.hod()
        global  hod
        hod+=1

    def pred(self):
        n = []
        s = 0
        self.pred_pole = Pole(width, height)
        for i in range(2**(self.width * self.height)):
            n = bin(i)
            s = 0
            for y in range(self.width):
                for x in range(self.height):
                    if s < len(n):
                        self.pred_pole.kletka(y, x).next_sost(n[s])
                        s += 1
                    else:
                        self.game_pole.kletka(y, x).next_sost(0)
                    self.game_pole.kletka(y, x).old_to_new()
            self.pred_pole.hod()
            if self.game_pole.kletki == self.pred_pole.kletki:
                break
        for i in range(width*height):
            if i % width == 0:
                print()
            if i < len(n):
                print(n[i], end=" ")
            else:
                print(0, end=" ")
        print()

    def anim(self):
        global anim
        n = []
        for y in range(self.width):
            for x in range(self.height):
                n.append(self.game_pole.kletka(x, y).sost())
        n.reverse()
        anim.append(des(n))

    def play(self):
        global anim
        pause = pygame.time.Clock()
        for i in anim:
            n = bin(i)
            s = 0
            for y in range(self.width):
                for x in range(self.height):
                    if s < len(n):
                        self.game_pole.kletka(x, y).next_sost(n[s])
                        s += 1
                        self.game_pole.kletka(x, y).old_to_new()
                    else:
                        self.game_pole.kletka(x, y).next_sost(0)
                        self.game_pole.kletka(x, y).old_to_new()
            gui.p()
            pause.tick(fps)

    def event(self):
        global fps
        global game
        global hod
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
                if i.key == pygame.K_LEFT and hod > 0:
                    n = bin(znat[hod-1])
                    s = 0
                    for y in range(self.width):
                        for x in range(self.height):
                            if s < len(n):
                                self.game_pole.kletka(x, y).next_sost(n[s])
                                s += 1
                                self.game_pole.kletka(x, y).old_to_new()
                            else:
                                self.game_pole.kletka(x, y).next_sost(0)
                                self.game_pole.kletka(x, y).old_to_new()
                    gui.p()
                    hod -=1
                if i.key == pygame.K_SPACE:
                    game *= -1
                if i.key == pygame.K_p:
                    self.pred()
                if i.key == pygame.K_s:
                    self.anim()
                if i.key == pygame.K_d:
                    global anim
                    anim = []
                if i.key == pygame.K_a:
                    self.play()
                    gui.p()
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
    while x != 0:
        ch.append(x % 2)
        x //= 2
    return ch

def des(x):
    x.reverse()
    ch = 0
    s = 0
    while(len(x)>s):
        ch += x[s]*(2**s)
        s += 1
    return ch

if __name__ == '__main__':
    print(des([1, 1, 1]))
    pause = pygame.time.Clock()
    gui = GUI()
    gui.p()
    while (True):
        gui.event()
        if game > 0:
            gui.hod()
            gui.p()
            pause.tick(fps)
