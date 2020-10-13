from datetime import date
class Skink:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

alex = Skink("Alex", "skink")

class Gecko:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

greg = Gecko("Greg", "gecko")

class Iguana:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

mary = Iguana("Mary", "iguana")

class Boa:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

bob = Boa("Bob", "boa")

class CornSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

gabe = CornSnake("Gabe", "corn snake")