# Indentations matter for python if-else blocks,
# so always add ":" after these stmt conditions
temperature = 15

if temperature >= 30:
    print("It's warm")
    print("Drink water")
elif temperature >= 20:
    print("It's pleasant")
else:
    print("It's chilly")

age = 30
# Ternary operator in python
message = "Eligible" if age > 18 else "Not Eligible"
print(f"message: {message}")

high_income = False
good_credit = True
is_student = False

# &, ! and || operator in python - all combined in a single stmt
if (high_income or good_credit) and not is_student:
    print("Eligible for loan!")
else:
    print("Not eligible")

if age < 18:
    print("is child")
# in python, comparisons can directly be written like this
elif 18 <= age < 65:
    print("Is adult")
else:
    print("Is senior citizen")
