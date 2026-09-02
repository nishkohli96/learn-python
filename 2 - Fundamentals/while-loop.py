# Loop 1: Iterate on a number
number = 100
while number > 0:
    print(number)
    number //= 2

# Loop 2: Iterate on a string
print("--- Type something and press enter; type \"quit\" to exit ---")
command = ""
while command.lower() != 'quit':
    command = input(">")
    print(f"ECHO: {command}")

# Loop 3: Infinite loop with break stmt
print("--- Infinite loop again; type \"quit\" to exit ---")
while True:
    user_input = input(">")
    print(f"ECHO: {user_input}")
    if user_input.lower() == 'quit':
        break

print("--- End of program ---")
