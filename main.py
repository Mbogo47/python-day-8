# Simple function
def greet():
    print("Hello")
    print("Where are you?")
    print("Are you fine?")


greet()


# Function that allows input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Where are you {name}?")
    print(f"Are you fine {name}?")


greet_with_name("Ivy")


# Functions with more than 1 input (Positional arguments)
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Ivy", "Kutus")


# Functions with Keyword argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(location="Kutus", name="Ivy")
