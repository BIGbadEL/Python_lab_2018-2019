import random


class Automat:
    def __init__(self, N, reg, rand):
        self.ciag = [random.randint(0, 1) if rand else 0 for _ in range(N)]
        self.ciag[N // 2] = 1 if not rand else self.ciag[N // 2]
        self.output = [self.ciag]
        reg = bin(reg)
        self.reg = []
        for ch in reg[2:]:
            self.reg.append(int(ch))
        for index in range(len(self.reg), 8):
            self.reg = [0] + self.reg
        print(self.reg)

    def evol(self):
        x = self.ciag[:]
        for i in range(len(self.ciag)):
            self.ciag[i] = self.reg[x[-i + 1] * 4 + x[i] * 2 + (x[-i - 1]) if i != len(x) - 1 else x[0]]
        self.output.append(self.ciag[:])

    def __str__(self):
        result = ""
        for x in self.output:
            for el in x:
                result += "*" if el else " "
            result += "\n"
        return result


a = Automat(50, 90, False)
print(a.ciag)
print(a.reg)
for _ in range(200):
    a.evol()
print(a.ciag)

print(a)
