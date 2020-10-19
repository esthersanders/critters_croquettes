from datetime import date
from .animal import Animal
from movements import Walking, Swimming


class Duck(Animal, Walking, Swimming):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, shift, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def run(self):
        print(f'{self} waddles')

