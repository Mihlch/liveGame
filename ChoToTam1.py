class kletka(object):
    def __init__(self, x, y, s):
        x.self = x
        y.self = y
        s.self = s
    def sost(self):
        return s.self
    def izsost(self, n):
        s.self = n
    def sosed(self, n):
        if n == 5:
            n = 9
        if n%3 == 1:
            x = x.self -1
        elif n == 2 or n == 8:
            x = x.self
        else:
            x = x.self + 1
        if n < 4:
            y = y.self - 1
        elif n < 7:
            y = y.self
        else:
            y = y.self + 1
        return x, y

class pole(object):
    def __init__(self, x, y):
        stolb.self = []
        pole.self = []
        for i in rnge(y):
            stolb.self.append(0)
        for i in range(x):
            pole.append(stolb.self)


def Hod(self, masiz, maspe):
    sk = 0
    x = 0
    y = 0
    for a in masiz:
        for b in a:
            for c in range(8):
                x, y = b.sosed(c)
                if masiz[x][y].sost() == 1:
                    sk += 1
            if b.sost() == 0:
                if sk >= 3:
                    maspe[x][y].izsost(1)
            else:
                if sk <4 and sk >1:
                    maspe[x][y].izsost(0)
            sk = 0


