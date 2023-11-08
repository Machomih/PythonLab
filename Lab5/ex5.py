class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    def display_info(self):
        return f"Species: {self.species}, Habitat: {self.habitat}"


class Mammal(Animal):
    def __init__(self, species, habitat, sound):
        super().__init__(species, habitat)
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} makes the sound: {self.sound}"


class Bird(Animal):
    def __init__(self, species, habitat, wingspan):
        super().__init__(species, habitat)
        self.wingspan = wingspan

    def fly(self):
        return f"The {self.species} is flying with a wingspan of {self.wingspan} meters"


class Fish(Animal):
    def __init__(self, species, habitat, water_type):
        super().__init__(species, habitat)
        self.water_type = water_type

    def swim(self):
        return f"The {self.species} is swimming in {self.water_type} water"


mammal = Mammal("Cow", "Forest", "Woof")
print(mammal.display_info())
print(mammal.make_sound())
print()

bird = Bird("Eagle", "Mountains", 2.5)
print(bird.display_info())
print(bird.fly())
print()

fish = Fish("Shark", "Ocean", "Salted")
print(fish.display_info())
print(fish.swim())
