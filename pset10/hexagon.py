class Hexagon:
    def __init__(self, lengthSide):
        self.lengthSide = lengthSide
    
    def calculate_perimeter(self):
        return 6 * self.lengthSide


hex = Hexagon(3)
print(hex.calculate_perimeter())