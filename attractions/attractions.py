class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def append(self, animal):
        self.animals.append(animal)

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithery creatures to admire"
        self.animals = list()

    def append(self, animal):
        self.animals.append(animal)

class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "silly swimmers"
        self.animals = list()

    def append(self, animal):
        self.animals.append(animal)