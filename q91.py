class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog says Woof!")

animal = Animal()
dog = Dog()

animal.speak()  # Output: The animal makes a sound.
dog.speak()     # Output: The dog says Woof!
