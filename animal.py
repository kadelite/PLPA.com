class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        pass
        
    def speak(self):
        pass

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs enthusiastically! 🐕")
        
    def speak(self):
        print("Woof! Woof!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims gracefully through the water. 🐟")
        
    def speak(self):
        print("Blub blub...")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies through the sky! 🦅")
        
    def speak(self):
        print("Tweet tweet!")

class Snake(Animal):
    def move(self):
        print(f"{self.name} slithers silently across the ground. 🐍")
        
    def speak(self):
        print("Hiss...")

# Demonstrate polymorphism
def animal_race(animals):
    print("🏁 And they're off! 🏁")
    for animal in animals:
        animal.move()

if __name__ == "__main__":
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Sky"),
        Snake("Viper")
    ]
    
    animal_race(animals)
    
    print("\nNow let's hear them speak:")
    for animal in animals:
        print(f"{animal.name} says: ", end="")
        animal.speak()