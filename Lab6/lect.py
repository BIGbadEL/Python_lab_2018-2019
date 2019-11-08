import random


def fib():
    x = 1
    y = 1
    while True:
        x, y = y + x, x
        yield x


def parzyste(seq):
    for el in seq:
        if el % 2:
            yield el


def niewieksze(seq, num):
    for el in seq:
        if el <= num:
            yield el
        else:
            return


g = sum(parzyste(niewieksze(fib(), 100)))  # niewieksze(parzyste(fib()), 100)

print(g)


####### 2

def myrange(first=0, last=None, c=1):
    if last is None:
        if first < 0:
            return
        last, first = first, 0
    elif last < first and c >= 0:
        return
    elif last > first and c <= 0:
        return

    if last < first:
        while last - c < first:
            first = first + c
            yield first
    else:
        while last > first:
            first = first + c
            yield first


for i in myrange(3):
    print(i)

for i in myrange(4, 2):
    print(i)

for i in myrange(2, 4):
    print(i)

for i in myrange(-4):
    print(i)

for i in myrange(4, 2, -1):
    print(i)


########## 3

def gener():
    x = random.random()
    y = random.random()
    while y > 0.1:
        if abs(x - y) < 0.4:
            yield y, x
        x = y
        y = random.random()


for i in gener():
    print(i)

####### 4

N = 20

bits = [random.randrange(2) for _ in range(N)]
print(bits)


def num_of_zeros(seq):
    number = 0
    for el in seq:
        if el == 0:
            number = number + 1
        elif number != 0:
            yield number
            number = 0


odleg = [el for el in num_of_zeros(bits)]
print(sum(odleg) / len(odleg))


######## 5

def rest(kwota, nominal):
    C = [k for k in range(kwota+1)]
    for i in nominal:
        for j in range(kwota + 1):
            if j >= i:
                C[j] = min(C[j], 1 + C[j-i])
        yield C


for cos in rest(20, [1, 2, 3, 4]):
    print(cos)
