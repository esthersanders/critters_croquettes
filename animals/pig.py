# import the python datetime module to help us create a timestamp
from datetime import date
from .animal import Animal
from movements import Walking


class Pig(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, shift, species, food, chip_num)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} and only ate after a long walk')

    def __str__(self):
        return f"{self.name} is a {self.species}"

