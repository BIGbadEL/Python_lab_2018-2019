import math
import numpy
import scipy
import matplotlib


class Point:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    def __init__(self):
        self.x = 0
        self.y = 0


def dekz(punkt1, punkt2):
    def dek(fun):
        def inner(p1, p2):
            if punkt1 <= p1.x <= punkt2 and punkt1 <= p1.y <= punkt2:
                return fun(p1, p2)
            else:
                raise ArithmeticError

        return inner

    return dek


@dekz(-10, 10)
def add(p1, p2):
    p = Point()
    p.x = p1.x + p2.x
    p.y = p1.y + p2.y
    return p


@dekz(-10, 10)
def sub(p1, p2):
    p = Point()
    p = p1.x - p2.x
    p = p1.y - p2.y
    return p


p1 = Point()
p2 = Point()
p3 = Point()
p3.x = 0
p3.y = 1
p2.x = 1
p = add(p1, p2)
print(p.x)
p.y = 1


class Count:
    def Pole(*args):
        boki = []
        for i in range(len(args)):
            next_i = (i + 1) if i != len(args) - 1 else 0
            bok = pow(args[i].x - args[next_i].x, 2) + pow(args[i].y - args[next_i].y, 2)
            bok = math.sqrt(bok)
            boki.append(bok)

        obw = sum(boki)
        s = obw / 2
        p = 1
        for b in boki:
            p *= (s - b)

        if (len(args) == 3):
            p = math.sqrt(p * s)
        else:
            p = math.sqrt(p)

        return obw, p


print(Count.Pole(p1, p2, p, p3))


class funktor:
    counter = {}

    def __init__(self, fun):
        self.fun = fun
        funktor.counter.setdefault(self.fun, 0)

    def __call__(self, *args, **kwargs):
        funktor.counter[self.fun] += 1
        self.fun(*args, **kwargs)

    def print():
        for k, val in funktor.counter.items():
            print(k.__name__, val)


@funktor
def fun1():
    pass


@funktor
def fun2():
    pass


@funktor
def fun3():
    pass


fun1()
fun1()
fun3()

funktor.print()
