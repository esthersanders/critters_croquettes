# import the python datetime module to help us create a timestamp
from datetime import date
from .animal import Animal
from movements import Walking


class Llama(Animal, Walking):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, shift, food, chip_num)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} after a bath')
