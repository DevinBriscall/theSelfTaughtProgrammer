class Square:

    squarelist = []

    def __init__(self, l):
        self.length = l
        self.squarelist.append(self.length)
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

square0 = Square(4)
square1 = Square(2)
square2 = Square(3)

print(Square.squarelist)
print(square0)