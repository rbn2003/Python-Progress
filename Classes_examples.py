class Animals:
    """A simple animal class"""

    def __int__(self, species, animal_name):
        self.species = species
        self.animal_name = animal_name

    def bipedal_movement(self):
        """Simulate how a bipedal animal walks"""
        movement_type = f"The animal{self.animal} is walking upright!"
        return movement_type
    
    def quad_movement(self):
        """Simulate how a quadrupal animal walks!"""
        movement_type = f"The{self.animal_name} is walking on all fours!"
        return movement_type

first_animal = Animals('primate', 'human')
print(f"Our first animal is a {first_animal.species}, and is {first_animal.animal_name}!")
print(first_animal.bipedal_movement())
print(first_animal.quad_movement())
