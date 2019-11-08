import random
import matplotlib.pyplot as plt


def fun(x = 0, y = 0, i = 10000):
    zestaw_wsp = [(0, 0, 0, 0, 0.16, 0), (0.2, -0.26, 0, 0.23, 0.22, 1.6), (-0.15, 0.28, 0, 0.26, 0.24, 0.44),
                  (0.85, 0.04, 0, -0.04, 0.85, 1.6)]
    with open("out.dat", "w") as file:
        for _ in range(i):
            actual = random.choices(zestaw_wsp, [1, 7, 7, 85])
            tempx = actual[0][0] * x + actual[0][1] * y + actual[0][2]
            y = actual[0][3] * x + actual[0][4] * y + actual[0][5]
            x = tempx
            file.write(f"{x} {y}\n")


def calka(start, stop, miny, maxy, fun):
    t = 0
    for n in range(1, 1000000):
        x = random.uniform(start, stop)
        y = random.uniform(miny, maxy)
        if fun(x) > y > 0:
            t += 1
        elif 0 > y > fun(x):
            t += -1

        if abs(3.14 * (t / n) - 2) < 1e-6:
            print(3.14 * t / n)
            return n


def integral(start, stop, fun):
    res = stop - start
    out = 0
    for n in range(1, 1000000):
        out += fun(random.uniform(start, stop))
        if abs(out / n * res - 2) < 1e-6:
            print(out / n * res)
            return n
