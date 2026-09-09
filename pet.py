class Pet:
    def __init__(self, name, animal_type):
        """Initialize pet attributes with default hunger and energy levels."""
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5

    def feed(self):
        """Reduce hunger by 1 when fed."""
        self.hunger -= 1
        print(f"{self.name} enjoyed the food!")
        print(f"Hunger level: {self.hunger}")