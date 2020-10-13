# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

miss_fuzz = Llama("Miss_Fuzz", "llama")

class Pig:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

wilbur = Pig("Wilbur", "pot-bellied pig")

class Donkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

eeyore = Donkey("Eeyore", "donkey")

class Rabbit:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

bugs = Rabbit("Bugs", "rabbit")

class Goat:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

bonnie = Goat("bonnie", "goat")