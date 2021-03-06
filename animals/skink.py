from datetime import date
from .animal import Animal 
from movements import Slithering

class Skink(Animal, Slithering):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, shift, species, food, chip_num)
        Slithering.__init__(self)
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} and only ate if no one was watching')

    def __str__(self):
        return f"{self.name} is a {self.species}"

