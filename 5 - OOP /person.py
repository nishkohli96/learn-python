class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


person1 = Person("Palak", 30)
person2 = Person("Rahul", 28)

print(person1.name)
print(person1.age)
print(person1.introduce())

print(person2.name)
print(person2.age)


class Calculator:
    def add(self, a, b):
        return a + b


calculator = Calculator()
print(calculator.add(10, 20))


class OnlyPerson:
    species = "Human"

    def __init__(self, name):
        self.name = name


person_1 = OnlyPerson("Rakesh")
print(OnlyPerson.species)
OnlyPerson.species = "Homo sapiens"
# "Homo sapiens" as the class attribute has been modified
print(person_1.species)

person_2 = OnlyPerson("Ramesh")
person_2.species = "Aam Aadmi"
print(person_2.species)


# Inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()

dog.eat()
dog.bark()

# Overriding Methods


class Animal1:
    def speak(self):
        print("Some sound")


class Dog1(Animal1):
    def speak(self):
        print("Woof woof!!")


doggie = Dog1()
doggie.speak()

# super


class Animal2:
    def __init__(self, name):
        self.name = name


class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Super() is for calling a method from the parent class explicitly,
# even when the child class has its own version of that method
# (or wants to extend it rather than fully replace it).
#
class Animal3:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def describe(self):
        return f"This is {self.name}"

class Dog3(Animal3):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # extend the parent's version instead of fully rewriting it
        parent_sound = super().speak()
        return f"{parent_sound}, specifically a bark"

dog = Dog3("Rex", "Labrador")
print(dog.speak())
# Rex makes a sound, specifically a bark

print(dog.describe())
# This is Rex   <- inherited unchanged, no override needed at all

# When you'd skip super() and fully override instead — if the
# child's behavior should completely replace the parent's, not build on it.
class Cat(Animal3):
    def speak(self):
        return f"{self.name} says meow"   # totally independent, no super() call
