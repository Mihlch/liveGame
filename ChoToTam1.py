import random
from pprint import pprint as pp

import pygame

game = True

class Kletka(object):
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.sold = s
        self.snew = s

    def sost(self):
        return self.sold

    def next_sost(self, n):
        self.snew = n

    def old_to_new(self):
        self.sold = self.snew

    def cord(self):
        return self.x, self.y


class Pole(object):


    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.kletki = []
        for i in range(self.height):
            self.kletki.append([])
            for j in range(self.width):
                self.kletki[i].append(Kletka(j, i, random.randint(0, 1)))
        #pp(self.kletki)

    def sosed(self, corde):
        s = 0
        x = corde[0]
        y = corde[1]
        s += self.kletki[(x + 1) % self.height][(y + 1) % self.width].sost()
        s += self.kletki[(x + 1) % self.height][(y - 1) % self.width].sost()
        s += self.kletki[(x + 1) % self.height][y].sost()
        s += self.kletki[(x - 1) % self.height][(y - 1) % self.width].sost()
        s += self.kletki[(x - 1) % self.height][(y + 1) % self.width].sost()
        s += self.kletki[(x - 1) % self.height][y].sost()
        s += self.kletki[x][(y + 1) % self.width].sost()
        s += self.kletki[x][(y - 1) % self.width].sost()
        return s


    def hod(self):
        schizm = 0
        for a in self.kletki:
            for b in a:
                sosedi = self.sosed(b.cord())
                if b.sost() == 0:
                    if sosedi >= 3:
                        b.next_sost(1)
                        schizm += 1
                else:
                    if sosedi < 2 or sosedi > 3:
                        b.next_sost(0)
                        schizm += 1
        for a in self.kletki:
            for b in a:
                b.old_to_new()

        global game
        if schizm == 0:
            game = False

    def wifth_and_height(self):
        return self.width, self.height

    def kletka(self, x, y):
        return self.kletki[x][y]



