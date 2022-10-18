# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   name = input("What is your name?\n")
#   print(f"Hello, {name}!")
#   print(f"I hope you are doing well today,{name}.\n\n")
#
# greet()
#
# Function with an input
# def greet_with_name(name):
#   print(f"Hello, {name}!")
#   print(f"I hope you are doing well today, {name}.")
#
# greet_with_name("Cameron")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"The weather in {location} is beautiful today, isn't it.")


# greet_with("Cameron", "Denver")
greet_with(location="Denver", name="Cameron")
