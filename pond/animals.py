from datetime import date

class Turtle:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

tim = Turtle("Tim", "box turtle")

class Duck:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

moriah = Duck("Moriah", "mallard")

class Otter:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

patrick = Otter("Patrick", "otter")

class Catfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

chuck = Catfish("Chuck", "catfish")

class Stingray:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

steve = Stingray("Steve", "stingray")