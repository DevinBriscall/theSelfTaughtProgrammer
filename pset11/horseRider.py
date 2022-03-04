class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, age, name, rider):
        self.age = age
        self.name = name
        self.rider = rider


george = Rider("George Shrinks")
horse = Horse(6, "Bullet", george)
print(horse.rider.name)
