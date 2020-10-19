from .attractions import Attraction
class SnakePit(Attraction):

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
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal.name} doesn\'t like to slither, so please do not put it in the {self.attraction_name} attraction.')

