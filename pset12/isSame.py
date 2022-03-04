def isSame(object1, object2):
    return object1 is object2

class Square:
    def __init__(self, length):
        self.length = length


square0 = Square(4)
square1 = Square(4)
square2 = square0

print(isSame(square0, square1))
print(isSame(square0, square2))