import math


################ 1


class it:
    def __init__(self, x, a):
        self.x = x
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.x > 100:
            raise StopIteration
        self.x += self.a
        return self.x


a = it(10, 20)

for i in a:
    for j in a:
        print(i, j)


class itv2:
    def __init__(self):
        self.x = 10
        self.a = 20

    def __iter__(self):
        return itv2()

    def __next__(self):
        if self.x > 100:
            raise StopIteration
        self.x += self.a
        return self.x


a = itv2()

for i in a:
    for j in a:
        print(i, j)


##################### 2


class T:
    def __init__(self):
        self.tab = [1]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.tab) > 20:
            raise StopIteration
        temp = []
        self.tab = self.tab + [0]
        for i in range(0, len(self.tab)):
            x = self.tab[i - 1] if i - 1 >= 0 else 0
            temp.append(x + self.tab[i])
        self.tab, temp = temp, self.tab
        return temp[:-1]


for i in T():
    print(i)


################### 3


class Los:
    def __init__(self):
        self.x = 1
        self.m = 2 ** 48
        self.a = 44485709377909

    def __iter__(self):
        return self

    def __next__(self):
        self.x = ((self.a * self.x) % self.m)
        return self.x / self.m


iter = Los()

in_circle = 0
in_squer = 0

for p1 in iter:
    p2 = next(iter) * 2 - 1
    p1 = p1 * 2 - 1
    in_squer += 1
    if p1 ** 2 + p2 ** 2 < 1:
        in_circle += 1

    if abs(4 * in_circle / in_squer - math.pi) < 1e-7:
        print(4 * in_circle / in_squer)
        print(in_squer)
        break
