# Object Oriented Programming

## Classes & Objects

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

`person1 = Person("Raj", 30)` is equivalent to:

`Person.__init__(person1, "Raj", 30)`

Therefore `self` refers to the current object. `self.name`, `self.age` are called **Instance Attributes**.

### Methods

**A function inside a class is called a method.**

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
```

Methods Can Accept Other Arguments

```py
class Calculator:
	  # self absorbs the auto-passed instance
    def add(self, a, b):
        return a + b

calculator = Calculator()
print(calculator.add(10, 20))
```

If you drop self, the method still gets called the normal way, but it'll break the moment Python tries to actually call it — because Python automatically passes the instance as the first argument to any method called on an instance, whether you wrote a parameter for it or not.

```py
calc = Calculator()
calc.add(2, 3)
TypeError: Calculator.add() takes 2 positional arguments but 3 were given.
```

Why 3, when you only passed 2?
Because Python automatically inserts the instance (calc) as the first argument to any method called via instance.method(...).

One case where it "works" without error — calling it on the class itself, not an instance:

```py
class Calculator:
    def add(a, b):
        return a + b
Calculator.add(2, 3)   # 5 — works! No instance auto-passed here
```

This works because you're calling add directly on the class, not on an instance — so there's no automatic instance-injection happening, and a=2, b=3 binds exactly as written.

### Class Attributes

```py
class Person:
    species = "Human"      # class attribute

    def __init__(self, name):
        self.name = name   # instance attribute
```
`species` is a class attribute. It belongs to the class rather than being unique to each object. So for each object of this class, its value would remain the same.

### __dict__
`__dict__` is a real built-in attribute every object automatically has — it's the actual storage dictionary holding an object's data. But instances and classes have separate __dict__s that store different things.

`instance.__dict__` — holds instance attributes only, not methods.

`ClassName.__dict__` — this is where methods (and properties) actually live

```py
class Person:
    def __init__(self, age):
        self.age = age

    def greet(self):
        return "hello"

p = Person(25)
print(p.__dict__)
# {'age': 25}

print(Person.__dict__.keys())
# dict_keys(['__module__', '__qualname__', '__init__', 'greet', '__dict__', '__weakref__', '__doc__'])
```

## Inheritance

```py
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()
dog.bark()
```

## Magic/Dunder methods
Magic methods (also called dunder methods — "double underscore", like `__init__`, `__str__`) are special methods Python automatically calls in response to built-in syntax and operations `—`, `+`, `len()`, `print()`, `==`, `[]`, `for`, etc. Defining them on your class lets your own objects hook into that built-in syntax instead of behaving like a "dumb" custom object.

```py
class Point:
    def __init__(self, x, y):        # called by Point(x, y)
        self.x = x
        self.y = y

    def __repr__(self):               # unambiguous, dev-facing representation
        return f"Point({self.x}, {self.y})"

    def __str__(self):                # readable, user-facing representation
        return f"({self.x}, {self.y})"
```

| Dunder | Triggered by | Purpose |
| __init__ | ClassName(...) | Constructor |
| __repr__ | repr(obj) ,REPL display | Developer-facing representation |
| __str__ | str(obj), print(obj) | User-facing representation |
| __eq__ | obj1 == obj2 | Value equality |
| __lt__, __gt__, etc. | <, >, sorting | Ordering/comparison |
| __add__, __sub__, etc. | +, -, etc. | Arithmetic operators |
| __len__ | len(obj) | Length |
| __getitem__ |obj[i] | Indexing (and enables basic iteration) |
| __contains__ | x in obj | Membership testing |
| __call__ | obj(...) | Makes instances callable like functions |
| __enter__ / __exit__ | with obj:	Context manager (setup/teardown) |

### name vs _name vs __name

1. `name` — Public (no underscore)
Freely accessible and modifiable from anywhere, no restriction, no special behavior.

```py
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Ramesh")
print(s.name)      # Ramesh  - direct access, totally normal
s.name = "Rahul"   # works fine, nothing stops it
print(s.name)      # Rahul
```

Use this when there's genuinely nothing to protect — most simple attributes fall here.

2. `_name` — Protected (single underscore, convention only)

Signals: "this is internal to the class (or its subclasses) — don't touch it from outside, even though I technically can't stop you." Python enforces nothing here; it's purely a courtesy signal for other developers and linters.

```py
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self._gpa = gpa   # "internal-ish" - a hint, not a lock

s = Student("Ramesh", 3.8)
print(s._gpa)     # 3.8 - still works! Python does NOT block this
s._gpa = 10.0     # also works, no error, even though it's a nonsense GPA
```

A single underscore is just a "handle with care" sticky note. It's commonly used for attributes/methods meant to be used by the class itself or subclasses, but not by external code.

```py
class Base:
    def _helper(self):   # meant for internal/subclass use
        return "internal logic"

    def public_method(self):
        return self._helper()   # used internally
```

3. `__name` — Private (double underscore, name-mangled)

This is the one where Python actually does something: it automatically renames the attribute internally to `_ClassName__name`, making it awkward (not impossible) to access accidentally from outside.

```py
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa   # double underscore

s = Student("Nishant", 3.8)

print(s.__gpa)
# AttributeError: 'Student' object has no attribute '__gpa'
```

It's not actually gone — Python just renamed it:

```py
print(s._Student__gpa)   # 3.8  - still technically reachable, just ugly/discouraged
```

Why does this "mangling" exist? Mainly to avoid naming collisions in subclasses, not really for security:

```py
class Base:
    def __init__(self):
        self.__value = "base"   # becomes _Base__value

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = "child"   # becomes _Child__value - different slot!

c = Child()
print(c.__dict__)
# {'_Base__value': 'base', '_Child__value': 'child'}
```

Both `__value` attributes coexist without clobbering each other, because mangling made their real names different. That's the actual designed purpose — not "true privacy," but collision-safety across inheritance.

## Encapsulation

Encapsulation is the OOP principle of bundling data (attributes) and the methods that operate on that data together inside a class, while restricting direct access to some of that data from outside — so an object controls how its internal state gets read or modified, rather than exposing it freely.


The core idea

Instead of letting outside code poke directly at an object's internals, you expose a controlled interface (methods) and hide the messy/sensitive details behind it.

```py
class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # freely accessible - no protection

account = BankAccount(100)
account.balance = -5000   # nothing stops this - invalid state, but Python allows it
```

Python's approach — naming conventions, not hard enforcement

1. Public (default) — no leading underscore:
```py
self.balance = balance   # anyone can access/modify freely
```

2. Protected (convention only) — single leading underscore _:
```py
self._balance = balance
```

Signals "internal use, don't touch this from outside the class/subclasses" — but Python doesn't actually stop you; it's purely a convention other developers (and linters) respect.

3. Private (name-mangled) — double leading underscore __:

```py
self.__balance = balance
```

Python actually renames this internally to _BankAccount__balance, making accidental external access harder (though not impossible if someone knows the mangled name).

**Why bother — what encapsulation actually buys you**

1. **Validation/invariants** — an object can guarantee its own data never enters an invalid state (as shown, no negative balances).
2. **Hides implementation details** — callers use account.balance, account.deposit(50) without knowing/caring whether it's stored as a float, tracked via a ledger, fetched from a database, etc. You can change internals later without breaking anyone using the class.
3. **Reduces coupling** — outside code depends on a stable interface (method names), not on your class's internal structure.

| Prefix | Convention meaning | Actually enforced? |
| - | - | - | 
| name | Public |	No restriction |
| _name | Protected — internal use | No, convention only |
| __name | Private | Name-mangled, harder to access accidentally |

## Polymorphism

Definition: Polymorphism ("many forms") means different classes can respond to the same method call in their own way — you call the same method name on different objects, and each object's own implementation runs, without the calling code needing to know or care which specific class it's dealing with.

```py
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo"
```

```py
animals = [Dog("Rex"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(animal.speak())

# Rex says Woof
# Whiskers says Meow
# Bessie says Moo
```

Without polymorphism, you'd have to write ugly type-checking branches everywhere:
```py
# Without polymorphism - brittle, and grows worse with every new animal type
def make_speak(animal):
    if isinstance(animal, Dog):
        print(f"{animal.name} says Woof")
    elif isinstance(animal, Cat):
        print(f"{animal.name} says Meow")
    elif isinstance(animal, Cow):
        print(f"{animal.name} says Moo")
    # ...and so on, forever, for every new class you add
```

The two flavors of polymorphism

1. Method overriding  — a subclass provides its own version of a method already defined in the parent (this is the common OOP form, and connects directly to the super() — you can override and extend via super().speak(), or override and fully replace ).

2. Duck typing — Python doesn't even require a shared parent class for polymorphism to work; if an object has the method being called, Python doesn't care what class it is. ("If it walks like a duck and quacks like a duck...")

> Polymorphism = the ability to call the same method name on objects of different types, and have each one respond in its own way — the caller doesn't need to know or check which exact type it's dealing with.

## Methods

| Method          | First argument        | Used for                  |
| --------------- | --------------------- | ------------------------- |
| Instance method | `self`                | Instance/object data      |
| Class method    | `cls`                 | Class-level data/behavior |
| Static method   | Nothing automatically | Utility behavior          |

```py
class Example:

    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```

## Composition

Composition is building complex objects by combining other objects as parts ("has-a" relationships) rather than inheriting from a parent class ("is-a" relationships). Instead of a class extending another class's behavior, it contains an instance of another class and delegates work to it.

The core distinction: "has-a" vs "is-a"
- Inheritance — `Dog` is an `Animal`. Shares behavior through a class hierarchy.
- Composition — `Car` has an `Engine`. Built by combining separate, independent objects.

```py
# Inheritance - "is-a"
class Dog(Animal):
    ...

# Composition - "has-a"
class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an Engine, isn't one
```

### Example

```py
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine starting with {self.horsepower} HP"

class GPS:
    def navigate(self, destination):
        return f"Navigating to {destination}"

class Car:
    def __init__(self, make, horsepower):
        self.make = make
        self.engine = Engine(horsepower)   # composed
        self.gps = GPS()                    # composed

    def start(self):
        return f"{self.make}: {self.engine.start()}"

    def navigate(self, destination):
        return self.gps.navigate(destination)

car = Car("Toyota", 180)
print(car.start())              # Toyota: Engine starting with 180 HP
print(car.navigate("Bengaluru")) # Navigating to Bengaluru
```

**Why prefer composition over inheritance (a well-known OOP principle: "favor composition over inheritance")**
Problem with deep inheritance — rigid, fragile hierarchies.

### Composition vs inheritance — quick comparison
| | Inheritance | Composition |
|-|-|-|
| Relationship | "is-a" | "has-a" |
| Coupling | Tight — subclass depends on parent's internals |	Loose — depends only on the composed object's public interface |
| Flexibility |	Fixed at class definition |	Swappable at runtime (pass different objects in)
| Risk | Deep hierarchies get rigid/fragile ("fragile base class" problem) | More boilerplate (explicit delegation methods sometimes needed) |
| Good for | Genuine "kind of" relationships (Dog is an Animal) |	Assembling behavior from independent, reusable parts |

**Rule of thumb:** reach for inheritance only when the relationship is genuinely a specialization (a Dog really is a more specific Animal, sharing its whole nature). Reach for composition when you're really just reusing functionality or assembling a bigger object out of smaller, independent pieces — which, in real-world codebases, is the more common and more flexible need.

## Abstraction
Abstraction — hide complexity, expose only what's needed

Expose a simple, essential interface while hiding the internal implementation details. This is the one pillar we haven't built an example for yet — it's usually done via abstract base classes, forcing subclasses to implement certain methods without saying how:

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every shape MUST implement this - but Shape itself doesn't say how."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

Shape()
# TypeError: Can't instantiate abstract class Shape with abstract method area

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.area())   # caller doesn't care HOW area is computed, just that it IS
```

**Comparing OOP Principles:**

| Pillar | Answers the question | Example |
| - | - | - |
| Encapsulation | "How do I protect an object's internal state?" | Person.age property/setter |
| Inheritance | "How do I reuse/share behavior between related classes?" | Dog(Animal) |
| Polymorphism | "How do I write code that works across different types uniformly?" |	speak() overridden per animal |
| Abstraction |	"How do I define what must be done without dictating how?" | Shape.area() abstract method |
