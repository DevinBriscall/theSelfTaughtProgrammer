from os import lseek


class Square:
    def __init__(self, l):
        self.length = l
    
    def calculate_perimeter(self):
        return self.length * 4


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)


square = Square(4)
rec = Rectangle(4, 5)
print(square.calculate_perimeter())
print(rec.calculate_perimeter())