# --- Class Method ---
# A class method receives the class as its first argument instead of the instance.
# Class methods — need access to the class itself, not a specific instance (cls)
# Used with `@classmethod` — commonly for alternative constructors, or anything
# that needs to read/modify class-level (shared) state rather than one instance's data.

class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species


print(Person.get_species())

class BankAccount:
    interest_rate = 0.02   # class attribute, shared by all accounts

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_string(cls, data_string):
        """Create an account from 'owner,balance' format, e.g. loading from a CSV row."""
        owner, balance = data_string.split(",")
        # cls() = calls BankAccount(...) here
        return cls(owner, float(balance))

    @classmethod
    def set_interest_rate(cls, rate):
        """Changes the rate for ALL accounts, not just one."""
        cls.interest_rate = rate

    @staticmethod
    def is_valid_amount(amount):
        """Pure validation logic - doesn't need self or cls at all."""
        return isinstance(amount, (int, float)) and amount > 0

# Normal construction
acc1 = BankAccount("Lucky", 1000)

# Alternative constructor - parsing a differently-shaped input
acc2 = BankAccount.from_string("Rahul,2500")
print(acc2.owner, acc2.balance)   # Rahul 2500.0

# Changes a value shared across ALL instances
BankAccount.set_interest_rate(0.03)
print(acc1.interest_rate)   # 0.03 - changed for existing instances too
print(acc2.interest_rate)   # 0.03

# Another example
# import datetime
#
# d = datetime.date.today()        # classmethod - alternative constructor
# d2 = datetime.date.fromtimestamp(1723600000)  # another classmethod constructor


# --- Static Method ---
# A static method doesn't automatically receive either self or cls.
# Used with @staticmethod — a plain function that's grouped inside the class
# for organizational/namespacing reasons, but doesn't touch instance or class state at all.
#
# Why put it inside a class if it doesn't use the class?
# -> Usually because the function is conceptually related to the class.

print(BankAccount.is_valid_amount(500))    # True
print(BankAccount.is_valid_amount(-50))    # False

# Also callable on an instance (works, but conceptually you're not using instance data)
acc = BankAccount("Divya", 1000)
print(acc.is_valid_amount(500))    # True

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
print(MathUtils.add(10, 20))
