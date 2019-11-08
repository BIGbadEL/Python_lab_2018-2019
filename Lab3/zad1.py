# random(), randInt(), randRange(), shuffle(), choice(), sample(seq, count), choices(seq, waga)
# slowaniki pop del get(klucz, cozwraca jak niema), popItem - losowa para, update(innyslownik) - dodwanie slownikow
# iterownaie for k in slownik, item , values, item - pary, setDefault(klucz, wartosc)

import random
import math
from sys import argv, exit


def is_prime(number):
    if number == 1:
        return False

    dzielnik = 1

    while dzielnik <= math.sqrt(number):
        if not number % dzielnik:
            return False
        dzielnik += 1

    return True


slownik = {}

while len(slownik) <= 50:
    new_elem = random.randint(0, 99)
    slownik.setdefault(new_elem, is_prime(new_elem))

print(slownik)

keyS = [random.randrange(20) for _ in range(100)]

print(keyS)

parzyste = {}
nieparzyste = {}
for index, el in enumerate(keyS):
    if not el % 2:
        parzyste.setdefault(el, []).append(index)
    else:
        nieparzyste.setdefault(el, []).append(index)

print(parzyste)
print(nieparzyste)

kolejny_slownik = {k: old_list if len([el for el in old_list if not el % 3]) != 0 else (max(old_list), min(old_list))
                   for k, old_list in parzyste.items()}

print(kolejny_slownik)

if len(argv) == 1:
    exit()

dictionary = {}

for key in range(int(argv[1])):
    dictionary.setdefault(key, random.randrange(2, 15))

print(dictionary)

lista_krotek = [(k, elem) for k, elem in dictionary.items()]
print(lista_krotek)

lista_krotek = {k: elem for k, elem in dictionary.items()}
new_dictionary = {}
for a, b in lista_krotek.items():
    new_dictionary.setdefault(b, []).append(a)

print(new_dictionary)

elements = [random.randrange(11) for _ in range(100)]
print(elements)

piaty_slownik = {}
for el in elements:
    piaty_slownik.setdefault(el, []).append(
        elements.index(el, 0 if not piaty_slownik[el] else piaty_slownik[el][-1] + 1))

print(piaty_slownik)

six_one = {}
six_two = {}

for i in range(10):
    six_one.setdefault(i, random.randrange(1, 100))
    six_two.setdefault(i, random.randrange(1, 100))

one_six = {x: k for k, x in six_one.items()}
two_six = {x: k for k, x in six_two.items()}

print(six_one)
print(one_six)

# one_six.update(two_six)

lastone = {k: (war1, two_six[k]) for k, war1 in six_one.items() if k in two_six}
print(lastone)
