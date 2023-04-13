
class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def __str__(self):
        return f'Calculator({self.num_1}, {self.num_2})'
    def __add__(self, other):
        return Calculator(self.num_1 + other.num_1, self.num_2 + other.num_2)
    def __sub__(self, other):
        return Calculator(self.num_1 - other.num_1, self.num_2 - other.num_2)
    def __mul__(self, other):
        return Calculator(self.num_1 * other.num_1, self.num_2 * other.num_2)
    def __truediv__(self, other):
        return Calculator(self.num_1 / other.num_1, self.num_2 / other.num_2)

c1 = Calculator(2, 10)
c2 = Calculator(5, -2)
c3 = Calculator(3, 3)

print(c1 + c2 - c3)
print(c1 / c2)