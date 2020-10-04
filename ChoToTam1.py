class kletka(object):
    def __init__(self, x, y, s):
        x.self = x
        y.self = y
        s.self = s
    def sost(self):
        return s.self
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


def Hod(self, masiz, maspe):
    sk = 0
    x = 0
    y = 0
    for a in masiz:
        for b in i:
            for c in range(8):
                x, y = b.sosed(c)
                if masiz[x][y].sost() == 1:
                    sk += 1

        sk = 0


if __name__ == '__main__':
    print(123)