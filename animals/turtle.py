from datetime import date
from .animal import Animal
from movements import Walking, Swimming


class Turtle(Animal, Walking, Swimming):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, shift, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        
       
        

    # @property 
    # def chip_number(self):
    #     return self.__chip_number

    # @chip_number.setter
    # def chip_number(self, number):
        pass
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

