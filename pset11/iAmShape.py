


class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("i am a shape")

class Square(Shape):
    def __init__(self, l):
        self.length = l
    
    def calculate_perimeter(self):
        return self.length * 4


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)



square = Square(4)
square.what_am_i()
rec = Rectangle(4, 5)
rec.what_am_i()