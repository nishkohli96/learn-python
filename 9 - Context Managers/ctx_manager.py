class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext():
    print("Inside context")

# Output -
# Entering context
# Inside context
# Exiting context


class MyContextErr:
    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")
        print(exc_type)
        print(exc_value)
        print(traceback)


with MyContextErr():
    print("Inside")
    raise ValueError("Something went wrong")
