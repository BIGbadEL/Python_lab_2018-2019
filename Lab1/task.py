from math import sqrt
from cmath import sqrt as csqrt
from sys import argv

print(type(argv))
print(argv)

if argv.__len__() < 4:
    print("error")
else:
    a = float(argv[1])
    b = float(argv[2])
    c = float(argv[3])

    delta = b ** b - 4 * a * c

    if delta < 0:
        x1 = (-b + csqrt(delta)) / (2 * a)
        print("x1 = ", x1, " x2 = ", x1.real - x1.imag * 2j)
    elif delta == 0:
        x = (-b + sqrt(delta)) / (2 * a)
        print("x1 = ", x)
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("x1 = ", x1, " x2 = ", x2)
