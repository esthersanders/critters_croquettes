from .attractions import Attraction
from movements import Walking

class PettingZoo(Attraction):
    
    def __init__(self, name, description):
        super().__init__(name, description)
        self.animals = list()

    def append(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]

    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal.name} now lives in {self.attraction_name}")
        else:
            print(f'{animal.name} doesn\'t like to be petted, so please do not try to put it in the {self.name} attraction.')