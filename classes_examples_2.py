class Animals():
    """A simple animal class"""
    def __init__ (self, species, animal_name):
        """Initialize animal species and name atrributes!"""
        self.species = species
        self.animal_name = animal_name


    def bipedal_movement(self):
        """Simulate how a bipedal animal walks"""
        movement_type = f"The {self.animal_name} is walking upright!"
        return movement_type

    def quad_movement(self):
        """Simulate how Quadrupdeal animal walks"""
        movement_type = f"The {self.animal_name} is walking on all fours!"
        return movement_type

animal_1 = Animals('primate', 'human')
print(f"Animal_1 is a {animal_1.species} and is {animal_1.animal_name}") 
print(animal_1.bipedal_movement())

animal_behavior_2 = animal_1.quad_movement()
print(animal_behavior_2) 