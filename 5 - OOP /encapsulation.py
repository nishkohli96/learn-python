# A property allows you to make something look like an attribute
# while executing logic behind it. In this case "balance" is a property
# of the class BankAccount
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # hidden internal state

    # Because of the @property/@balance.setter pair, account.balance
		# still reads/writes like a normal attribute syntactically
		# — but every write now runs through your validation logic first.
		# That's encapsulation in practice: the internal representation (__balance)
		# is hidden, and all interaction happens through a controlled interface.
    @property
    def balance(self):
        """Getter — read access"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter — controlled write access, with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

account = BankAccount(100)

print(account.balance)     # 100 — reads via the getter, looks like a plain attribute
account.deposit(50)
print(account.balance)     # 150

# ValueError: Balance cannot be negative   <- now actually protected
# account.balance = -5000

# AttributeError: 'BankAccount' object has no attribute '__balance'
# (it's actually stored as account._BankAccount__balance internally)
# print(account.__balance)

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value

p = Person(25)

try:
    p.age = -100
except ValueError as e:
    print(f"Couldn't update age: {e}")

# 25 — read via the getter. unchanged due to the error, the assignment never completed
print(p.age)
print(p._age) # 25 — the real underlying value (works, just discouraged by convention)
print(p.__dict__) # {'_age': 25} — no 'age' key at all, only '_age'

print(Person.__dict__.keys())
# <property object at 0x...>  ← the property lives on the class
print(Person.__dict__['age'])

# Step 1 — what self.age = age inside __init__ actually does:
#   This is the key thing to internalize: because age is decorated
#   as a @property (with a setter defined), self.age = age does not
#   create a plain attribute called age. Instead, Python intercepts
#  this assignment and routes it through the setter method — it's
#   exactly equivalent to writing:
#   def age(self, value):        # the setter
#     if value < 0:
#        raise ValueError("Age cannot be negative")
#     self._age = value 
#  
# Step 2 — so _age is created inside the setter, not in __init__ directly.
#   __init__ never touches _age itself. It just does self.age = age, which
#   indirectly causes _age to be set, because that assignment gets redirected
#   into the setter's logic (including the validation check).

# Trace it with a concrete example:
#
# p = Person(25)
# __init__(self, 25) runs.
# self.age = 25 → since age is a property with a setter, this calls the setter: age(self, 25).
# 
# Inside the setter: 25 < 0 is False, so no error.
# self._age = 25 executes — this is the actual attribute creation.
# Now self.__dict__ contains {'_age': 25} — note: no age key at all, only _age.
#
# Now, reading p.age:
# print(p.age)   # 25
# This calls the getter:
# @property
# def age(self):
#   return self._age   # reads the real stored value
#
# Why do it this roundabout way instead of just self.age = value
# directly in __init__ with a plain attribute?
# -> Because this way, construction goes through the same validation
#  as any later assignment:
# python
# p = Person(-5)
# ValueError: Age cannot be negative
#
# If __init__ had instead written directly to self._age = age
# (bypassing the property), construction would skip validation
# entirely — you could construct a Person(-5) with no error,
# and only get validation on later reassignment (p.age = -5).
# Routing through self.age = age (the public property name)
# in __init__ ensures validation applies uniformly,
# both at construction time and at any point after.
#
# If I were to handle error in class __init__, it silently loses
# the protection your @property setup gives you

class InvalidPerson:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age          # write directly to storage, bypass the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value        # no validation here anymore

# p = InvalidPerson(-5) # error here
# p.age = -100        # no error at all!
# print(p.age) 
#
# — the object's actual stored state (_age) is never touched
# when validation fails. The object stays exactly as it was
# before the bad assignment attempt. This is exactly the safety
# guarantee properties are meant to provide: an object can never
# be left in an invalid, half-updated state.
