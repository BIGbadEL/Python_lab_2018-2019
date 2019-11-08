import sys

sys.path.append("/home/grzegorz/PycharmProjects/Laboratoria/Lab13/build/lib.linux-x86_64-3.7")
import mod
import random
from time import time


def sortpy(tab):
    for _ in range(len(tab)):
        for j in range(len(tab) - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


print(mod.met(1, 2, 3))

tab1 = [random.randint(10, 100) for _ in range(100)]
tab2 = tab1[:]
start = time()
mod.mysort(tab1)
print(time() - start)

start = time()
sortpy(tab2)
print(time() - start)
print(mod.mysrd(tab2))
print(mod.mymed(tab2))
tab = {random.randint(10, 100): random.randint(10, 100) for _ in range(10)}

print(tab)
print(mod.mynwd(tab))

n = 4

for i in range(1, n):
    with open(f"plik{i}.dat", "w") as file:
        for _ in range(n):
            val = [0, random.randint(1, n)]
            file.write(str(random.choices(val, [50, 50])[0]) + "\n")

dict = {}

for i in range(1, n):
    with open(f"plik{i}.dat", "r") as file:
        for j in range(n):
            val = int(file.readline())
            if val:
                dict.setdefault(j, []).append(val)


res = []
for i in range(1, n):
    if len(dict[i]) > 30:
        res.append(mod.mymed(dict[i]))
    else:
        res.append(mod.mysrd(dict[i]))


print( dict)
print(res)