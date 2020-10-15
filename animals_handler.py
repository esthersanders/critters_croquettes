
from slither import Skink, Gecko, Iguana, Boa, Cornsnake
from pond import Turtle, Duck, Otter, Catfish, Stingray
from pet import Llama, Pig, Donkey, Rabbit, Goat
from attractions import PettingZoo, SnakePit, Wetlands


miss_fuzz = Llama("Miss_Fuzz", "llama", "afternoon", "llama chow")
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(miss_fuzz.feed())

wilbur = Pig("Wilbur", "pot-bellied pig", "midday", "slop")
print(wilbur.feed())

eeyore = Donkey("Eeyore", "donkey", "morning", "")

bugs = Rabbit("Bugs", "rabbit", "afternoon", "food")

bonnie = Goat("bonnie", "goat", "midday", "grass")


tim = Turtle("Tim", "box turtle", "bugs")

moriah = Duck("Moriah", "mallard", "food")

patrick = Otter("Patrick", "otter", "food")

chuck = Catfish("Chuck", "catfish", "food")

steve = Stingray("Steve", "stingray", "food")


alex = Skink("Alex", "skink", "insects")

greg = Gecko("Greg", "gecko", "insects")

mary = Iguana("Mary", "iguana", "insects")

bob = Boa("Bob", "boa", "insects")

gabe = Cornsnake("Gabe", "corn snake", "insects")

print(gabe)

varmint_village = PettingZoo("Varmint Village")
varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(wilbur)
varmint_village.animals.append(eeyore)
varmint_village.animals.append(bugs)
varmint_village.animals.append(bonnie)

slither_inn = SnakePit("Slither Inn")
slither_inn.animals.append(alex)
slither_inn.animals.append(greg)
slither_inn.animals.append(mary)
slither_inn.animals.append(bob)
slither_inn.animals.append(gabe)


critter_cove = Wetlands("Critter Cove")
critter_cove.animals.append(tim)
critter_cove.animals.append(moriah)
critter_cove.animals.append(patrick)
critter_cove.animals.append(chuck)
critter_cove.animals.append(steve)


for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')
