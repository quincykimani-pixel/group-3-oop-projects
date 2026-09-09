class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    print(f"Hi! My name is {self.name} and I am {self.age} years old.")

class Club:
  def __init__(self, name):
    self.name = name
    self.members = []

  def add_member(self, student):
    self.members.append(student)
    print(f"{student.name} joined {self.name}!")

  def show_members(self):
    print(f"Members of {self.name}:")
    for member in self.members:
        print(member.name)

student1 = Student("Alice", 18)
student2 = Student("Brian", 19)
student3 = Student("Faith", 18)
gaming_club = Club("Gaming Club")
robotics_club = Club("Robotics Club")
gaming_club.add_member(student1)
gaming_club.add_member(student2)
robotics_club.add_member(student3)
gaming_club.show_members()
robotics_club.show_members()

