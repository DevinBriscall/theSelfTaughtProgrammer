import math

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r * self.r * math.pi

circle = Circle(2)
print(circle.area())