class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
           
    def area(self):
        return self.base * (self.height / 2)

triangle = Triangle(3, 7)
print(triangle.area())