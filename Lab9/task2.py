import math


class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        return self + other

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                   self.x * other.y - self.y * other.x)

    def triple_product(self, other1, other2):
        return self.cross(other2).dot_product(other1)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        if key == 1:
            self.y = value
        if key == 2:
            self.z = value


a = Vec(1, 2, 3)
b = Vec(2, 3, 4)
c = Vec(2, 7, 20)

a += b

print(a)
print(a[2])
a[1] = 200
print(a)
print(a.triple_product(b, c))
