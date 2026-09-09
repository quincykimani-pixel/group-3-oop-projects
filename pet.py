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

    def play(self):
        """Increase hunger by 1 and decrease energy by 1 when playing."""
        self.hunger += 1
        self.energy -= 1
        print(f"{self.name} is playing!")

    def status(self):
        """Print current status and attributes of the pet."""
        print(f"--- {self.name} ---")
        print(f"Type: {self.animal_type}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")

# Run interaction script
if __name__ == "__main__":
    pet1 = Pet("Milo", "Dog")
    pet2 = Pet("Luna", "Cat")

    pet1.status()
    pet1.feed()
    pet1.play()
    pet1.status()