from animals import Boa, Catfish, Cornsnake, Donkey, Duck, Gecko, Goat, Iguana, Llama, Otter, Pig, Rabbit, Skink, Stingray, Turtle
from attractions import PettingZoo, SnakePit, Wetlands

miss_fuzz = Llama("Miss_Fuzz", "llama", "afternoon", "llama chow", 59)
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(miss_fuzz.feed())

wilbur = Pig("Wilbur", "pot-bellied pig", "midday", "slop", 29)
print(wilbur.feed())

eeyore = Donkey("Eeyore", "donkey", "morning", "", 32)
print(eeyore.feed())

bugs = Rabbit("Bugs", "rabbit", "afternoon", "food", 116)

bonnie = Goat("bonnie", "goat", "midday", "grass", 789)


tim = Turtle("Tim", "box turtle", "morning", "bugs", 123789)

print(tim.chip_number)

moriah = Duck("Moriah", "mallard", "food", "afternoon", 1167)

patrick = Otter("Patrick", "otter", "food", "midday", 2345)

chuck = Catfish("Chuck", "catfish", "food", "morning", 5674)

steve = Stingray("Steve", "stingray", "food", "midday", 6785)


alex = Skink("Alex", "skink", "insects", "afternoon", 6780)

greg = Gecko("Greg", "gecko", "insects", "afternoon", 27382)

mary = Iguana("Mary", "iguana", "insects", "morning", 123772)

bob = Boa("Bob", "boa", "midday", "insects", 17238)

gabe = Cornsnake("Gabe", "corn snake", "insects", "midday", 9372)

print(gabe)

varmint_village = PettingZoo("Varmint Village", "cuddly creatures")
varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(wilbur)
varmint_village.animals.append(eeyore)
varmint_village.animals.append(bugs)
varmint_village.animals.append(bonnie)

slither_inn = SnakePit("Slither Inn", "slithery creatures")
slither_inn.animals.append(alex)
slither_inn.animals.append(greg)
slither_inn.animals.append(mary)
# slither_inn.animals.append(bob)
slither_inn.animals.append(gabe)


critter_cove = Wetlands("Critter Cove", "waterbound buddies")
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


print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(critter_cove.last_critter_added)

print(tim.run())
print(tim.swim())
print(moriah.run())

# remember, some animals may require more arguments than others; e.g. shift
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Turtle("Snappy", "American Alligator", "midday", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
varmint_village.add_animal_pythonic(snappy)

for animal in varmint_village.animals:
    print(animal)

critter_cove.add_animal_pythonic(bugs)

slither_inn.add_animal_pythonic(chuck)