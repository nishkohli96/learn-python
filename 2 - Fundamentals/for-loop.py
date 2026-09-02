# For loop iteration in python

# Loop 1: Runs from 0 to 3
for number in range(4):
    print("number", number)

print("----")

# Loop 2: Runs from 1 to 6
for i in range(1, 7):
    print("Iteration", i )

print("----")

# Loop 3: Runs from 1 to 9, with step 2 
for num in range(1, 10, 2):
    print("Attempt", num , "." * num)

# Loop 4: Iterating on a string
for char in "PyTh0n":
    print(char)

# Loop 5: For with else block
#
# 1. If sucess is "True", it would just print "successful" and exit.
# 2. If success is "False", it goes through all iterations and then
#    executes the else block.
success = False
max_tries = 3
for num in range(max_tries):
    print(f"Attempt #{num + 1}")
    if success:
        print("successful")
        break
else:
    print(f"Attempted {max_tries} times and failed")

# Loop 6: Iterating on a list
fruits = ["apple", "banana", "orange", "mango", "kiwi"]
for fruit in fruits:
    print(fruit)

# Loop 7: Iterating on a list with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("--- End of program ---")
