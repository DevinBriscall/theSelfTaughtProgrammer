class apple:
    def __init__(self, colour, weight, size, variety):
        self.colour = colour
        self.weight = weight
        self.size = size
        self.variety = variety

apple = apple("red", "12oz", "10cm", "red delicious")
print(apple.colour)