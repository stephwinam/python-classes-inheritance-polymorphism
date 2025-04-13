class Animal:
    def move(self):
        pass  # Base class move method 

class Dog(Animal):
    def move(self):
        print("Running on four legs.")

class Bird(Animal):
    def move(self):
        print("Flying with wings.")

class Fish(Animal):
    def move(self):
        print("Swimming with fins.")

# Creating instances of different animals
dog = Dog()
bird = Bird()
fish = Fish()

# Calling the move() method for each animal
dog.move()
bird.move()
fish.move()

