from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")

def make_pair(a: T, b: U) -> tuple[T, U]:
    return (a, b)

print(make_pair(10, "John"))
print(make_pair("hello", True))

# Constrained TypeVar
# Returns "int" if the input is an int, and "float" if the input is a float.
Number = TypeVar("Number", int, float)
def double(value: Number) -> Number:
    return value * 2

print(double(5))
print(double(3.14))

def add(a: Number, b: Number) -> Number:
    return a + b

add(1, 2)        # ✅ int
add(1.5, 2.5)    # ✅ float
add(1, 2.5)      # ❌ error - mixing int and float, not a single consistent type

# Bounded TypeVar

class Animal:
    def speak(self):
        ...

class Dog(Animal):
    pass


class Cat(Animal):
    pass

# Anml must be Animal or a subclass of Animal.
Anml = TypeVar("Anml", bound=Animal)

def get_animal(animal: Anml) -> Anml:
    return animal
