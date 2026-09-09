class Pet:
    def __init__(self, name, animal_type):
        """Initialize pet attributes with default hunger and energy levels."""
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5