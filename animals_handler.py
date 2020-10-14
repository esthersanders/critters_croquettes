
from slither import Skink, Gecko, Iguana, Boa, Cornsnake
from pond import Turtle, Duck, Otter, Catfish, Stingray
from pet import Llama, Pig, Donkey, Rabbit, Goat


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

# def main():
#         host = ''
#         port = 8088
#         HTTPServer((host, port), HandleRequests).serve_forever()


# if __name__ == "__main__":
#         main()