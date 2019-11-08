import random


def first(wyr):
    resulst = {}

    for i in range(0, random.randrange(0, 21)):
        x = random.random()

        resulst[x] = f'{eval(wyr.format(x)):.3f}'

    return resulst


print(first("2 * {} + 1"))


def drugi(*a):
    result = []
    for lista in a[0]:
        for elem in a[1:]:
            if lista not in elem:
                break
        else:
            result.append(lista)

    return result


print(drugi((2, 3), (2, 3)))


def trzeci(a, b, flag=True):
    length = min(len(a), len(b)) if flag else max(len(a), len(b))

    return [(x, b[a.index(x)] if a.index(x) < len(b) else None) for x in a]


print(trzeci((1, 3, 2), (2, 3, 8, 9, 0)))  # , False))


def maxim(*a):
    return max(a)


def czwarte(a, fun):
    return fun(*a)


print(czwarte([1, 2, 3, 4], maxim))


def piate(val, nom):
    result = {}

    for n in nom:
        count = 0
        temp = val
        while val >= n:
            val = val - n
            count = count + 1
        result[n] = count
        if not val:
            break
        if val == temp:
            print("niemozliwe")
            return None

    return result


print(piate(27, (10, 5, 2)))


def six(szukna, start, stop, typ='r'):
    kroki = 1
    proba = random.randrange(start, stop) if typ == 'r' else int((start + stop) / 2)
    while proba != szukna:
        kroki = kroki + 1
        newStart = proba if proba < szukna else start
        newStop = proba if proba > szukna else stop
        proba = random.randrange(newStart, newStop) if typ == 'r' else (newStart + newStop // 2)

    return kroki


print(six(2, 10, 30, ""))
