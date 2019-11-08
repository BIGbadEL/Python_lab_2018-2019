import mod
import math


if __name__ == "__main__":
    mod.fun()

    print(mod.calka(0, 3.14, 0, 1, lambda x: math.sin(x)))
    print(mod.integral(0, 3.14, lambda x: math.sin(x)))
