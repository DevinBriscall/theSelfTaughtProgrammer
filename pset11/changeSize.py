from re import S


class Square:
    def __init__(self, l):
        self.length = l

    def change_size(self, c):
        self.length += c

    def calc_perimeter(self):
        return self.length * 4

square = Square(4)
print(square.calc_perimeter())
square.change_size(3)
print(square.calc_perimeter())