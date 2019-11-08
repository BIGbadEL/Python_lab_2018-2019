from sys import argv, exit

if len(argv) < 2:
    print("Podaj argumetny programu")
    exit()

print(''.join(argv[1:]))
string = ''.join((argv[1:]))

small_letters = ''.join([lit for lit in string if (lit.islower() and not lit.isdigit())])
print(small_letters)

capital_letters = ''.join([lit for lit in string if lit.isupper() and not lit.isdigit()])
print(capital_letters)

numbers = ''.join([cyf for cyf in string if cyf.isnumeric()])

print(numbers)

other = ''.join([oth for oth in string if not oth.isalpha()])
print(other)


bezpow = []

for el in small_letters:
    if el not in bezpow:
        bezpow.append(el)

print(bezpow)

count_list = [(elem, small_letters.count(elem)) for elem in bezpow]

print(count_list)

count_list.sort(key=lambda x: x[1])
print(count_list)

samogloski = 'eEuUiIoOaA'

a = sum([string.count(el) for el in samogloski])


print(a)
b = len(small_letters) + len(capital_letters) - a

tuple_list = [(int(el), a * index + b) for index, el in enumerate(numbers)]

print(tuple_list)

X = [x for x, _ in tuple_list]
Y = [y for _, y in tuple_list]

srX = sum(X) / len(X)
srY = sum(Y) / len(Y)

D = sum((x - srX) ** (x - srX) for x in X)

a = sum(y * (x - srX) for x, y in tuple_list) / D

b = srY - a * srX

print(f"{a} * x + {b}")
