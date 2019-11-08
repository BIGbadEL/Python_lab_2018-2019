import math
import keyword
from copy import deepcopy


print('''Hello!''')

print(keyword.kwlist)

a = 1
print(type(a))
a = 'a'
print(type(a))
a = 1 / 2
print(type(a))

print(a)


a, *b = 1, 2, 'a'

print(a, b)

print(type(b))
a, b = b, a

print(a, b)

print(dir(math))

help(math.modf)

print(math.modf.__doc__)

print(pow(2, 3, 4))
print(math.pow(2, 3))

print(sum([1, 2, 3]))

print(math.hypot(3, 4))

print(2 ** 3)

niekrotka = (1)

print(type(niekrotka))

tuple = (1,)
print(type(tuple))

x = (1, 'a', (1, 2), [1, 2, 3])

print(x)
print(type(x))
print(len(x))

y = ([1, 2, 'a'], 1, 1.7, 'b')

y[0][1] = 3

print(y[0])
y = [[1, 2, 'a'], 1, 1.7, 'b']

y[0] = 5

print(y[0])

z = y

print(y)

print(id(y))
print(id(z))

z = y[:]  # [odktórego : doktórego]

print(id(y))
print(id(z))

z[0] = 2
y[2] = 'b'

print(y)
print(z)

z = deepcopy(y)

print(y)
print(z)

l = [[]] * 7

print(l)

l1 = [0] * 7

print(l1)

l1[1] = 3

print(l1)

l[1].append(3)
print(l)

list = [[] for _ in range(7)]
print(list)

list[1].append((3, 2, 3, 4))
list[1].extend((2, 3))

print(list)

# a = wart1 if warunek else wart2

for i in range(4, 1, -1):
    print(i)

list = [1, 2, 3, 4]

for i in list:
    i += 1

print(list)

for i in range(len(list)):
    list[i] += 1

print(list)

for i, el in enumerate(list):
    list[i] = el + 1
    if el > 1000:
        break
else:
    print("cos")

print(list)
