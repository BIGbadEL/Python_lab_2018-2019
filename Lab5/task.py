from time import time
from sys import version
import random
import math

powt = 1000
N = 100


def tester(function):
    for _ in range(powt):
        function(N)


def forStatement(number):
    result = []
    for el in range(number):
        result.append(el)


def listComprehension(number):
    result = [el for el in range(number)]


def mapFunction(number):
    result = map(lambda x: x, range(number))


def generatorExpression(number):
    result = (el for el in range(number))


print(version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    ti = time()
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
    print(time() - ti)

# zad 2


first = [random.randrange(20) for _ in range(100)]
second = [random.randrange(20) for _ in range(100)]

print(list(filter(lambda x: x if 15 > sum(x) > 3 else None, zip(first, second))))


# zad 3

def errors(x, y):
    Xsr = sum(x) / len(x)
    Ysr = sum(y) / len(y)
    D = sum(xi ** 2 for xi in map(lambda xi: xi - Xsr, x))
    a = sum(map(lambda yi, xi: yi * xi, y, map(lambda xi: xi - Xsr, x))) / D
    b = Ysr - a * Xsr
    deltaY = math.sqrt(sum(map(lambda yi, xi: (yi - (a * xi + b)) ** 2, x, y)) / (len(x) - 2))
    deltaA = deltaY / math.sqrt(D)
    deltaB = deltaY * math.sqrt(1 / len(x) + Xsr / D)
    return a, deltaA, b, deltaB


print(errors([1, 2, 3], [1, 2, 3]))


# zad 4

def myreduce(fun, lista):
    result = lista[0]
    for el in lista[1:]:
        result = fun(result, el)

    return result


print(myreduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(myreduce(lambda x, y: x * y, [1, 2, 3, 4]))


# zad 5

def five(points):
    # return list(map(lambda x: x[0], points)), list(map(lambda y: y[1], points))
    return myreduce(lambda point, cos: map(lambda x, y: [x, y] if not isinstance(x, list) else x + [y], point, cos), points)


print(list(five([[1, 4], [2, 5], [3, 6]])))


