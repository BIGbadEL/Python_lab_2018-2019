import abc
import types
import math
import random


#
# class A(object):
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")
#
#
# a = B()
#
# print(B.mro())
#
#
# class W:
#     def __init__(self):
#         print("W")
#
#
# class A(W):
#     def __init__(self):
#         super().__init__()
#         print("A")
#
#
# class V:
#     def __init__(self):
#         print("V")
#
#
# class B(V):
#     def __init__(self):
#         super().__init__()
#         print("B")
#
#
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         print("C")
#
#
# print(C.mro())
# c = C()

# class A:
#     __metaclass__ = abc.ABCMeta

# class A(abc.ABC):

class Calka(abc.ABC):
    def __init__(self, start, stop, fun):
        if not isinstance(start, (float, int)) or not isinstance(stop, (float, int)):
            raise TypeError("first/second arg is not a number")
        if not isinstance(fun, types.FunctionType):
            raise TypeError("last argument is not a function")
        self.start = start
        self.stop = stop
        self.fun = fun

    @abc.abstractmethod
    def value(self):
        pass


class CalkaT(Calka):
    def __init__(self, start, stop, fun):
        super().__init__(start, stop, fun)

    def value(self):
        step = math.fabs(self.stop - self.start) / 1000
        result = 0
        for i in range(1000):
            result += self.fun(self.start + i * step) + self.fun(self.start + (i + 1) * step)
        return result * step / 2


c = CalkaT(0, 2, lambda x: x)
print(c.value())


class CalkaS(Calka):
    def __init__(self, start, stop, fun):
        super().__init__(start, stop, fun)

    def value(self):
        step = math.fabs(self.stop - self.start) / 1000
        result = self.fun(self.start)
        for i in range(1, 1000, 2):
            result += 4 * self.fun(self.start + i * step)
        for i in range(2, 999, 2):
            result += 2 * self.fun(self.start + i * step)
        result += self.fun(self.stop)

        return result * step / 3


cs = CalkaS(0, 2, lambda x: x)
print(cs.value())


################################### 2


class Stos:
    def __init__(self, other=None):
        self.elements = []
        if other is not None:
            self.elements = other.elements[:]

    def size(self):
        return len(self.elements)

    def pop(self):
        return self.elements.pop(-1)

    def push(self, element):
        if isinstance(element, int):
            self.elements.append(element)
        elif isinstance(element, Stos):
            for i in range(element.size()):
                self.push(element.pop())

    def __str__(self):
        result = ""
        for el in self.elements:
            result += str(el) + "\n"
        return result


st = Stos()
st.push(1)
st.push(2)
st.push(3)

print(st)

st.pop()

print(st)


class sortStos(Stos):
    def __init__(self, other=None):
        if isinstance(other, sortStos):
            super().__init__(other)
        else:
            super().__init__()

    def push(self, element):
        if isinstance(element, int) and element >= self.elements[-1] if self.elements else True:
            self.elements.append(element)
        elif isinstance(element, sortStos):
            for i in range(element.size()):
                self.push(element.pop())


st = sortStos()
st.push(1)
st.push(2)
st.push(3)

print(st)

st.pop()

print(st)

print(st.size())

sizes = 0

for _ in range(100):
    stos = sortStos()
    for _ in range(100):
        stos.push(random.randint(0, 100))
    sizes += stos.size()

print(sizes / 100)


class wc:
    allletters = 0
    allwords = 0
    alllines = 0


    def __init__(self, file):
        self.file = file

    def count(self):
        with open(self.file, "r") as f:
            x = f.readlines()
            lines = len(x)
            words = 0
            letters = 0
            for el in x:
                words += len(el.split())
                letters += len(el)
            print(lines, words, letters, self.file)
            wc.allletters += letters
            wc.alllines += lines
            wc.allwords += words

    @staticmethod
    def printFiles():
        print(wc.alllines, wc.allwords, wc.allletters, "razem")




x = wc("task.py")
x.count()
x = wc("plik1.dat")
x.count()
x = wc("plik2.dat")
x.count()
x = wc("plik3.dat")
x.count()
x = wc("plik4.dat")
x.count()
x = wc("plik5.dat")
x.count()

wc.printFiles()
