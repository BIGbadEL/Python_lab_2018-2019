################## 1
import collections
import types


def fun(*seq):
    for el in seq:
        if not isinstance(el, float):
            raise TypeError("nielibczba")
    if sorted(seq) != seq:
        raise Exception("nieposortowany")

    return seq[int(len(seq) / 2)]


try:
    print(fun(*[3, 2, "string"]))
except Exception as Obj:
    print(Obj)


#################### 2

def fx(x):
    return x


def integral(func, start, stop, howmeny):
    if not isinstance(func, types.FunctionType):
        raise TypeError("first argument is not a function")
    if not isinstance(start, (float, int)):
        raise TypeError("second arg should be a number")
    if not isinstance(stop, (float, int)):
        raise TypeError("third arg should be a number")
    if not isinstance(stop, int):
        raise TypeError("fourth arg should be a int")
    step = abs(start - stop) / howmeny
    print(step)
    result = 0
    while start <= stop:
        result = result + func(start) * step
        start = start + step
    return result


try:
    print(integral(fx, 0, 1, 100))
except Exception as Obj:
    print(Obj)


################ 3


def trzy(seq, num):
    if not len(seq) % num:
        raise Exception("wrong number of elements in list")
    for i in range(0, len(seq) - num, num):
        try:
            if max(seq[i:i + num]) != seq[i + num - 1]:
                raise Exception(" wrong last element in " + str(seq[i: i + num]))
        except Exception as Obj:
            print(Obj)
        else:
            parzysee = 0
            for j in seq[i: i + num]:
                if j % 2 == 0:
                    parzysee = parzysee + 1
            print(str(seq[i: i + num]), sum(el * el for el in seq[i: i + num - 1]), seq[i + num - 1] * seq[i + num - 1])
            if sum(el * el for el in seq[i: i + num - 1]) == seq[i + num - 1] * seq[i + num - 1]:
                print(
                    str(seq[i: i + num]) + " to trójka pitagorejska parzyste " + str(parzysee) + " nieparzyste " + str(
                        num - parzysee))


l = (
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12,
    12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8, 11,
    16,
    21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2, 14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29, 2)

try:
    trzy(l, 3)
except Exception as Obj:
    print(Obj)

l = (
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12,
    12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8, 11,
    16,
    21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2, 14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29)

try:
    trzy(l, 3)
except Exception as Obj:
    print(Obj)

l = (3, 4, 5, 5, 12, 13, 7, 24, 25, 9, 40, 41, 6, 8, 10, 60, 80, 100, 18, 24, 30, 15, 8, 17)

try:
    trzy(l, 3)
except Exception as Obj:
    print(Obj)

l = (3, 4, 5, 5, 13, 12, 7, 24, 25, 9, 40, 41, 6, 8, 10, 60, 80, 100, 18, 24, 30, 15, 8, 17)

try:
    trzy(l, 3)
except Exception as Obj:
    print(Obj)


def aver(name):
    s1 = 0
    s2 = 0
    with open(name, "r") as file:
        data = file.readlines()
        if not data:
            raise ArithmeticError("pusty plik")
        first = []
        second = []

        for el in data:
            temp = el.split()
            if len(temp) < 2:
                raise ArithmeticError("zla liczba kolumn")
            for x in temp:
                if not x.isdigit():
                    raise ArithmeticError("zly typ")

            first.append(float(temp[0]))
            second.append(float(temp[1]))
        s1 = sum(first) / len(first)
        s2 = sum(second) / len(second)
    with open("srednia", "a") as file:
        file.write(str(s1) + " " + str(s2) + "\n")


try:
    aver("plik1.dat")
except ArithmeticError as err:
    print(err)

try:
    aver("plik2.dat")
except ArithmeticError as err:
    print(err)

try:
    aver("plik3.dat")
except ArithmeticError as err:
    print(err)

try:
    aver("plik4.dat")
except ArithmeticError as err:
    print(err)

try:
    aver("plik5.dat")
except ArithmeticError as err:
    print(err)
